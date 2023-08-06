# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Queries sent to devices during detection to determine their device type."""
import copy
import enum
import functools
import logging
import os
import re
import subprocess
import typing
from typing import Any, Callable, Collection, Dict, List, Union

from gazoo_device import config
from gazoo_device import errors
from gazoo_device import extensions
from gazoo_device.base_classes import auxiliary_device_base
from gazoo_device.base_classes import primary_device_base
from gazoo_device.capabilities.interfaces import switchboard_base
from gazoo_device.utility import host_utils
from gazoo_device.utility import http_utils
from gazoo_device.utility import pwrpc_utils
from gazoo_device.utility import usb_utils
import immutabledict
import requests

_DeviceClassType = Union[auxiliary_device_base.AuxiliaryDeviceBase,
                         primary_device_base.PrimaryDeviceBase]
_LOG_FORMAT = "<%(asctime)s> %(filename)-20s:%(lineno)d: %(message)s"

_ADB_COMMANDS = immutabledict.immutabledict({})

_DOCKER_COMMANDS = immutabledict.immutabledict({
    "PRODUCT_NAME": "docker ps --filter id={} --format {{{{.Names}}}}",
})

_SSH_COMMANDS = immutabledict.immutabledict({
    "IS_CHIP_TOOL_PRESENT": ("which", "chip-tool"),
    "UNIFI_PRODUCT_NAME": ("mca-cli-op", "info"),
    "RPI_PRODUCT_NAME": ("cat", "/proc/device-tree/model"),
    "IS_MATTER_LINUX_APP_RUNNING": (
        "pgrep", "-f", pwrpc_utils.MATTER_LINUX_APP_NAME)
})

_HTTP_ENDPOINTS = immutabledict.immutabledict({
    "DLI_PRODUCT_NAME": "http://{address}/restapi/config/=brand_name/"
})

# https://oidref.com/1.3.6.1.2.1.1.1
_GET_SYSTEM_DESCRIPTION_SNMP_COMMAND = (
    "snmpget -v 2c -c private {ip_address}:161 1.3.6.1.2.1.1.1.0")
# https://oidref.com/1.3.6.1.2.1.1.5
_GET_SYSTEM_NAME_SNMP_COMMAND = (
    "snmpget -v 2c -c private {ip_address}:161 1.3.6.1.2.1.1.5.0")
_DLINK_MODEL_RESPONSE_REG_EX = (
    r"((?:WS6-)?DGS-[0-9]+-[0-9]+)")
_SNMP_TIMEOUT_S = 5

_UNIFI_MODEL_PREFIXES = ("USW-", "US-")

_NRF_DK_COMMS_ADDRESS_LINUX = "SEGGER_J-Link"
_NRF_DK_EFR32_COMMS_ADDRESS_MAC = "tty.usbmodem"


@functools.total_ordering
class QueryEnum(enum.Enum):
  """Allows comparison of enum properties for sorting purposes."""

  def __lt__(self, other):
    return self.name < other.name  # pylint: disable=comparison-with-callable


class AdbQuery(QueryEnum):
  IS_SERIAL_NUMBER = "is_serial_number"


class DockerQuery(QueryEnum):
  PRODUCT_NAME = "product_name"


class GenericQuery(QueryEnum):
  ALWAYS_TRUE = "always_true"


class PigweedQuery(QueryEnum):
  """Query names for detection for PigweedSerialComms Devices."""
  IS_MATTER = "is_matter"
  IS_NRF_OPENTHREAD = "is_nrf_openthread"
  PRODUCT_NAME = "usb info product_name"
  MANUFACTURER_NAME = "usb info manufacturer_name"


class PtyProcessQuery(QueryEnum):
  PRODUCT_NAME = "product_name"


class SerialQuery(QueryEnum):
  ADDRESS = "address"
  IS_NRF_OPENTHREAD = "is_nrf_openthread"
  PRODUCT_NAME = "usb info product_name"
  SERIAL_NUMBER = "usb serial_numer"
  VENDOR_PRODUCT_ID = "VENDOR_ID:PRODUCT_ID"


class SnmpQuery(QueryEnum):
  """Query names for detection of SnmpComms Devices."""
  IS_DLINK = "is_dlink_power_switch"


class SshQuery(QueryEnum):
  """Query names for detection for SshComms Devices."""
  IS_DLI = "is_dli_power_switch"
  IS_RASPBIAN_RPI = "is_raspbian_raspberry_pi"
  IS_UBUNTU_RPI = "is_ubuntu_raspberry_pi"
  IS_UNIFI = "is_unifi_switch"
  IS_CHIP_TOOL_PRESENT = "is_chip_tool_installed_on_rpi"
  IS_MATTER_LINUX_APP_RUNNING = "is_matter_linux_app_running_on_rpi"


class UsbQuery(QueryEnum):
  PRODUCT_NAME = "usb product name"
  SERIAL_NUMBER = "serial_number"
  VENDOR_PRODUCT_ID = "VENDOR_ID:PRODUCT_ID"


def _docker_product_name_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Gets product name from docker device."""
  del create_switchboard_func  # Unused by _docker_product_name_query
  try:
    name = subprocess.check_output(
        _DOCKER_COMMANDS["PRODUCT_NAME"].format(address).split())
    name = name.decode()
  except subprocess.CalledProcessError as err:
    detect_logger.info(
        "_docker_product_name_query failed for %s: %r", address, err,
        exc_info=True)
    return ""
  return name


def _always_true_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Used when there is just one type of device for a communication type."""
  del address, create_switchboard_func, detect_logger  # Unused.
  return True


def _adb_is_serial_number_query(
    address: str,
    detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Returns True if address is a serial number, False if it's an IP address."""
  del create_switchboard_func, detect_logger  # Unused.
  return not re.search(host_utils.IP_ADDRESS, address)


def _is_dli_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines if address belongs to dli power switch."""
  del create_switchboard_func  # Unused by _is_dli_query
  try:
    response = http_utils.send_http_get(
        _HTTP_ENDPOINTS["DLI_PRODUCT_NAME"].format(address=address),
        auth=requests.auth.HTTPDigestAuth("admin", "1234"),
        headers={"Accept": "application/json"},
        valid_return_codes=[200, 206, 207],
        timeout=1)
    name = response.text
  except RuntimeError as err:
    detect_logger.info("_is_dli_query failed for %s: %r", address, err,
                       exc_info=True)
    return False
  return "Power Switch" in name


def get_dlink_model_name(ip_address: str) -> str:
  """Returns the model name of the Dlink switch at the ip_address.

  Expected response for supported dlink switch model should look like:

    "DGS-1100-<total-number-of-ports>" or
    "WS6-DGS-1210-<total-number-of-ports>"

  Depending on the dlink switch, this model identifier can be held in either
  the system name or system description OID, so both are checked here.

  Args:
    ip_address: The IP address to query for dlink model name.

  Raises:
    errors.DeviceError: When the dlink model is not contained in either the
    system name or system description OIDs.

  Returns:
    str: The model of the dlink switch.
  """
  system_description_cmd = _GET_SYSTEM_DESCRIPTION_SNMP_COMMAND.format(
      ip_address=ip_address)
  system_description_response = subprocess.check_output(
      system_description_cmd.split(), text=True, timeout=_SNMP_TIMEOUT_S)
  match_model = re.search(
      _DLINK_MODEL_RESPONSE_REG_EX, system_description_response)
  if match_model:
    return match_model.group(1)

  system_name_cmd = _GET_SYSTEM_NAME_SNMP_COMMAND.format(ip_address=ip_address)
  system_name_response = subprocess.check_output(
      system_name_cmd.split(), text=True, timeout=_SNMP_TIMEOUT_S)
  match_model = re.search(_DLINK_MODEL_RESPONSE_REG_EX, system_name_response)
  if match_model:
    return match_model.group(1)

  raise errors.DeviceError(
      f"Failed to retrieve model name from dlink_switch {ip_address}.\n"
      f"Sent commands {[system_description_cmd, system_name_cmd]} and"
      f"got responses {[system_description_response, system_name_response]}")


def _is_dlink_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines if address belongs to dlink switch."""
  del create_switchboard_func  # Unused by _is_dlink_query
  try:
    model = get_dlink_model_name(ip_address=address)
    detect_logger.info("Got response to sysDescr SNMP query: %s\n"
                       "_is_dlink_query response: True", model)
  except (subprocess.CalledProcessError, errors.DeviceError) as err:
    detect_logger.info("_is_dlink_query failure: %r", err, exc_info=True)
    return False
  return True


def _is_raspbian_rpi_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines if address belongs to raspberry pi."""
  del create_switchboard_func  # Unused by _is_raspbian_rpi_query
  try:
    name = host_utils.ssh_command(
        address,
        command=_SSH_COMMANDS["RPI_PRODUCT_NAME"],
        user="pi",
        key_info=config.KEYS["raspberrypi3_ssh_key"])
  except RuntimeError as err:
    detect_logger.info("_is_raspbian_rpi_query failed for %s: %r", address, err,
                       exc_info=True)
    return False
  return "Raspberry Pi" in name


def _is_ubuntu_rpi_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines if address belongs to raspberry pi Ubuntu."""
  del create_switchboard_func  # Unused by _is_ubuntu_rpi_query
  try:
    host_utils.ssh_command(
        address,
        command=_SSH_COMMANDS["RPI_PRODUCT_NAME"],
        user="ubuntu",
        key_info=config.KEYS["raspberrypi3_ssh_key"])
  except RuntimeError as err:
    detect_logger.info(
        "_is_ubuntu_rpi_query failed for %s: %r", address, err,
        exc_info=True)
    return False
  return True


def _is_matter_app_running_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines whether Matter linux app is running on an RPi."""
  del create_switchboard_func  # Unused by _is_matter_app_running_query
  try:
    host_utils.ssh_command(
        address,
        command=_SSH_COMMANDS["IS_MATTER_LINUX_APP_RUNNING"],
        user="ubuntu",
        key_info=config.KEYS["raspberrypi3_ssh_key"])
  except RuntimeError as err:
    detect_logger.info(
        "_is_matter_app_running_query failed for %s: %r", address, err,
        exc_info=True)
    return False
  return True


def _is_chip_tool_installed_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines whether chip-tool is installed on an RPI."""
  del create_switchboard_func  # Unused by _is_chip_tool_installed_query
  try:
    host_utils.ssh_command(
        address,
        command=_SSH_COMMANDS["IS_CHIP_TOOL_PRESENT"],
        user="pi",
        key_info=config.KEYS["raspberrypi3_ssh_key"])
  except RuntimeError as err:
    detect_logger.info(
        "_is_chip_tool_installed_query failed for %s: %r", address, err,
        exc_info=True)
    return False
  return True


def _is_unifi_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Determines if address belongs to unifi poe switch."""
  del create_switchboard_func  # Unused by _is_unifi_query
  try:
    mca_info = host_utils.ssh_command(
        address,
        _SSH_COMMANDS["UNIFI_PRODUCT_NAME"],
        user="admin",
        key_info=config.KEYS["unifi_switch_ssh_key"])
  except RuntimeError as err:
    detect_logger.info("_is_unifi_query failed for %s: %r", address, err,
                       exc_info=True)
    return False

  for model_prefix in _UNIFI_MODEL_PREFIXES:
    if model_prefix in mca_info:
      return True
  return False


def _pty_process_name_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Returns product name from pty process comms address directory.

  Args:
    address: The communication address.
    detect_logger: The logger of device interactions.
    create_switchboard_func: Method to create the switchboard.
  """
  del create_switchboard_func, detect_logger  # Unused.
  return address


def usb_product_name_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Gets product name from usb_info."""
  del create_switchboard_func, detect_logger  # Unused.
  return usb_utils.get_product_name_from_path(address).lower()


def _usb_serial_number_from_serial_port_path(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Gets serial number from serial port path."""
  del create_switchboard_func, detect_logger  # Unused.
  return usb_utils.get_serial_number_from_path(address)


def _usb_vendor_product_id_from_serial_port_path(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Gets USB vendor ID and product ID from serial port path."""
  del create_switchboard_func, detect_logger  # Unused.
  device_info = usb_utils.get_device_info(address)
  return f"{device_info.vendor_id}:{device_info.product_id}"


def _usb_product_name_from_serial_number(
    address: str,
    detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Returns USB product name from serial number.

  Args:
    address: Serial number of the device. USB devices are addressed by their
      serial number.
    detect_logger: The logger of device interactions.
    create_switchboard_func: Method to create the switchboard.

  Returns:
    Product name from USB descriptor.
  """
  del create_switchboard_func  # Unused
  device = usb_utils.get_usb_device_from_serial_number(address)
  detect_logger.info(
      "_usb_product_name_from_serial_number: USB device is %r", device)
  return device.product if device else ""


def _usb_vendor_product_id_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Returns USB vendor and product ID from serial number.

  Args:
    address: Serial number of the device. USB devices are addressed by their
      serial number.
    detect_logger: The logger of device interactions.
    create_switchboard_func: Method to create the switchboard.

  Returns:
    Vendor and product ID string of the USB device that has a matching
    serial number.
    Format of the string is VENDOR_ID:PRODUCT_ID in hex. E.g. '0ab1:fe23'.
    Returns empty string if address is not found.
  """
  del create_switchboard_func  # Unused by usb_vendor_product_id_query
  # Address contains serial number for USB devices
  device = usb_utils.get_usb_device_from_serial_number(address)
  detect_logger.info("_usb_vendor_product_id_query: USB device is %r", device)
  return f"{device.idVendor:04x}:{device.idProduct:04x}" if device else ""


def _get_communication_address(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Returns the communication address.

  This detection criteria should be used in conjunction with
  _usb_vendor_product_id_query to narrow down a match.

  For USB devices, this function is particularly useful to matching FTDI
  manufacturer IDs which should be consistent between products that use FTDI
  chipsets. The manufacturer's ID is the first two characters in the serial
  number.
  See:
  https://www.ftdichip.com/Support/Knowledgebase/howistheautomaticserialnu.htm

  Args:
    address: Communication address of the device. USB devices are addressed by
      their serial number.
    detect_logger: The logger of device interactions.
    create_switchboard_func: Method to create the switchboard.

  Returns:
    Communication address.
  """
  del create_switchboard_func, detect_logger  # Unused.
  return address


def _manufacturer_name_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> str:
  """Gets manufacturer name from usb_info."""
  del create_switchboard_func, detect_logger  # Unused.
  return usb_utils.get_device_info(address).manufacturer.lower()


def _is_matter_device_query(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Returns True if the device is a Matter device.

  Args:
    address: The communication address.
    detect_logger: The logger of device interactions.
    create_switchboard_func: Method to create the switchboard.

  Returns:
    True if the device is a Matter device, False otherwise.
  """
  file_handler = typing.cast(logging.FileHandler, detect_logger.handlers[0])
  log_path = file_handler.baseFilename
  return pwrpc_utils.is_matter_device(
      address, log_path, create_switchboard_func, detect_logger)


def _is_nrf_board(address: str) -> bool:
  """Returns if the address belongs to a NRF board."""
  return (_NRF_DK_COMMS_ADDRESS_LINUX in address or
          _NRF_DK_EFR32_COMMS_ADDRESS_MAC in address)


def _is_nrf_openthread(
    address: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> bool:
  """Returns True if the device is an NRF board with OpenThread CLI binary."""
  if not _is_nrf_board(address):
    return False
  file_handler = typing.cast(logging.FileHandler, detect_logger.handlers[0])
  log_path = file_handler.baseFilename
  switchboard = create_switchboard_func(communication_address=address,
                                        communication_type="SerialComms",
                                        device_name=os.path.basename(log_path),
                                        log_path=log_path)
  resp = switchboard.send_and_expect(
      command="invalid", pattern_list=[r".*InvalidCommand\n"], timeout=3)
  return resp.match is not None and not resp.timedout


GENERIC_QUERY_DICT = immutabledict.immutabledict({
    GenericQuery.ALWAYS_TRUE: _always_true_query,
})

ADB_QUERY_DICT = immutabledict.immutabledict({
    AdbQuery.IS_SERIAL_NUMBER: _adb_is_serial_number_query,
})

DOCKER_QUERY_DICT = immutabledict.immutabledict({
    DockerQuery.PRODUCT_NAME: _docker_product_name_query,
})

PIGWEED_QUERY_DICT = immutabledict.immutabledict({
    PigweedQuery.IS_MATTER: _is_matter_device_query,
    PigweedQuery.IS_NRF_OPENTHREAD: _is_nrf_openthread,
    PigweedQuery.PRODUCT_NAME: usb_product_name_query,
    PigweedQuery.MANUFACTURER_NAME: _manufacturer_name_query,
})

PTY_PROCESS_QUERY_DICT = immutabledict.immutabledict({
    PtyProcessQuery.PRODUCT_NAME: _pty_process_name_query,
})

SERIAL_QUERY_DICT = immutabledict.immutabledict({
    SerialQuery.ADDRESS: _get_communication_address,
    SerialQuery.IS_NRF_OPENTHREAD: _is_nrf_openthread,
    SerialQuery.PRODUCT_NAME: usb_product_name_query,
    SerialQuery.SERIAL_NUMBER: _usb_serial_number_from_serial_port_path,
    SerialQuery.VENDOR_PRODUCT_ID: _usb_vendor_product_id_from_serial_port_path,
})

SNMP_QUERY_DICT = immutabledict.immutabledict({
    SnmpQuery.IS_DLINK: _is_dlink_query,
})

SSH_QUERY_DICT = immutabledict.immutabledict({
    SshQuery.IS_DLI: _is_dli_query,
    SshQuery.IS_RASPBIAN_RPI: _is_raspbian_rpi_query,
    SshQuery.IS_UBUNTU_RPI: _is_ubuntu_rpi_query,
    SshQuery.IS_UNIFI: _is_unifi_query,
    SshQuery.IS_CHIP_TOOL_PRESENT: _is_chip_tool_installed_query,
    SshQuery.IS_MATTER_LINUX_APP_RUNNING: _is_matter_app_running_query,
})

USB_QUERY_DICT = immutabledict.immutabledict({
    UsbQuery.PRODUCT_NAME: _usb_product_name_from_serial_number,
    UsbQuery.SERIAL_NUMBER: _get_communication_address,
    UsbQuery.VENDOR_PRODUCT_ID: _usb_vendor_product_id_query,
})

DETECT_CRITERIA = immutabledict.immutabledict({
    "AdbComms": ADB_QUERY_DICT,
    "DockerComms": DOCKER_QUERY_DICT,
    "JlinkSerialComms": SERIAL_QUERY_DICT,
    "PigweedSerialComms": PIGWEED_QUERY_DICT,
    "PigweedSocketComms": SSH_QUERY_DICT,
    "PtyProcessComms": PTY_PROCESS_QUERY_DICT,
    "SerialComms": SERIAL_QUERY_DICT,
    "SnmpComms": SNMP_QUERY_DICT,
    "SshComms": SSH_QUERY_DICT,
    "UsbComms": USB_QUERY_DICT,
    "YepkitComms": GENERIC_QUERY_DICT,
})


def determine_device_class(
    address: str, communication_type: str, log_file_path: str,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> List[_DeviceClassType]:
  """Returns the device class(es) that matches the address' responses.

  Compares the device_classes DETECT_MATCH_CRITERIA to the device responses.

  Args:
    address: communication_address.
    communication_type: category of communication.
    log_file_path: local path to write log messages to.
    create_switchboard_func: Method to create the switchboard.

  Returns:
    list: classes where the device responses match the detect criteria.
  """
  detect_logger = _setup_logger(log_file_path)
  try:
    device_classes = get_communication_type_classes(communication_type)
    return find_matching_device_class(address, communication_type,
                                      detect_logger, create_switchboard_func,
                                      device_classes)
  finally:
    file_handler = detect_logger.handlers[0]
    file_handler.close()
    detect_logger.removeHandler(file_handler)


def find_matching_device_class(
    address: str, communication_type: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase],
    device_classes: Collection[_DeviceClassType]) -> List[_DeviceClassType]:
  """Returns all classes where the device responses match the detect criteria.

  Args:
    address: communication_address.
    communication_type: category of communication.
    detect_logger: logs device interactions.
    create_switchboard_func: Method to create the switchboard.
    device_classes: device classes whose match criteria must be compared to.

  Returns:
    list: classes where the device responses match the detect criteria.
  """
  matching_classes = []
  responses = _get_detect_query_response(address, communication_type,
                                         detect_logger, create_switchboard_func)
  detect_logger.info(
      "Possible %s device types: %s",
      communication_type,
      [device_class.DEVICE_TYPE for device_class in device_classes])
  for device_class in device_classes:
    if _matches_criteria(responses, device_class.DETECT_MATCH_CRITERIA):
      matching_classes.append(device_class)
      detect_logger.info("\t%s: Match.", device_class.DEVICE_TYPE)
    else:
      detect_logger.info("\t%s: No Match.", device_class.DEVICE_TYPE)
  return matching_classes


def get_communication_type_classes(
    communication_type: str) -> List[_DeviceClassType]:
  """Returns classes with that communication type.

  Args:
    communication_type: category of communication.

  Returns:
    list: classes with that communication type.
  """
  all_classes = copy.copy(extensions.auxiliary_devices)
  all_classes += copy.copy(extensions.primary_devices)
  all_classes += copy.copy(extensions.virtual_devices)
  matching_classes = []
  for device_class in all_classes:
    if device_class.COMMUNICATION_TYPE == communication_type:
      matching_classes.append(device_class)
  return matching_classes


def _get_detect_query_response(
    address: str, communication_type: str, detect_logger: logging.Logger,
    create_switchboard_func: Callable[..., switchboard_base.SwitchboardBase]
) -> Dict[str, Any]:
  """Gathers device responses for all queries of that communication type.

  Args:
    address: communication_address
    communication_type: category of communication.
    detect_logger: logs device interactions.
    create_switchboard_func: Method to create the switchboard.

  Returns:
    Device responses keyed by query enum member.
  """
  query_responses = {}
  detect_queries = extensions.detect_criteria[communication_type]
  for query_name, query in detect_queries.items():
    try:
      query_responses[query_name] = query(
          address=address,
          detect_logger=detect_logger,
          create_switchboard_func=create_switchboard_func)
      detect_logger.info("%s response from %s: %r",
                         query_name, address, query_responses[query_name])
    except Exception as err:  # pylint: disable=broad-except
      detect_logger.info("%s failed for %s: %r", query_name, address, err,
                         exc_info=True)
      query_responses[query_name] = repr(err)

    if not isinstance(query_responses[query_name], (str, bool)):
      detect_logger.warning(
          "%s returned invalid response type %s for %s!",
          query_name, type(query_responses[query_name]), address)

  return query_responses


def _matches_criteria(responses, match_criteria):
  """Checks if response dict matches match criteria.

  There are two categories of values in match_criteria: bool and regexp/str.
  Bools must match exactly, while regexp must find a match in the response
  value.

  Args:
    responses (dict): device responses keyed by query name.
    match_criteria (dict): match values keyed by query name.

  Returns:
    bool: whether or not responses meets match criteria
  """
  for entry, value in match_criteria.items():
    if isinstance(value, bool):
      if responses[entry] != value:
        return False
    else:
      if not re.search(value, responses[entry]):
        return False
  return True


def _setup_logger(log_file_path: str) -> logging.Logger:
  """Set up a logger to log device interactions to the detect file."""
  detect_logger = logging.getLogger(log_file_path)
  detect_logger.setLevel(logging.DEBUG)
  handler = logging.FileHandler(log_file_path)
  formatter = logging.Formatter(_LOG_FORMAT)
  handler.setFormatter(formatter)
  detect_logger.addHandler(handler)
  return detect_logger
