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
"""Matter controller capability using chip-tool command.

See
https://github.com/project-chip/connectedhomeip/tree/master/examples/chip-tool
for chip-tool usage and command references.
"""

import ast
import binascii
import os
import re
import shutil
import tempfile
import time
from typing import Any, Callable, List, Optional, Sequence

from gazoo_device import decorators
from gazoo_device import errors
from gazoo_device import gdm_logger
from gazoo_device.capabilities.interfaces import matter_controller_base
from gazoo_device.utility import http_utils
import immutabledict
import requests

logger = gdm_logger.get_logger()

_CHIP_TOOL_BINARY_PATH = "/usr/local/bin/chip-tool"
_HEX_PREFIX = "hex:"
_MATTER_NODE_ID_PROPERTY = "matter_node_id"
_MATTER_SDK_CERTS_DIRECTORY_PATH = "https://api.github.com/repos/project-chip/connectedhomeip/contents/credentials/development/paa-root-certs/"
_MATTER_SDK_REPO = "https://api.github.com/repos/project-chip/connectedhomeip/commits/master"
_RPI_TEMP_CERTS_DIR = "/tmp/chip_certs_folder_temp"
LOGGING_FILE_PATH = "/tmp/chip.log"
DEFAULT_PAA_TRUST_STORE_PATH = "/home/pi/certs"

_COMMANDS = immutabledict.immutabledict({
    "READ_CLUSTER_ATTRIBUTE":
        "{chip_tool} {cluster} read {attribute} {node_id} {endpoint_id}",
    "WRITE_CLUSTER_ATTRIBUTE":
        "{chip_tool} {cluster} write {attribute} {value} {node_id} "
        "{endpoint_id}",
    "SUBSCRIBE_CLUSTER_ATTRIBUTE_START":
        "nohup {chip_tool} interactive start < <(echo '{cluster} subscribe "
        "{attribute} {min_interval_s} {max_interval_s} {node_id} "
        "{endpoint_id}') > {logging_file_path} 2>&1 &",
    "SUBSCRIBE_CLUSTER_ATTRIBUTE_STOP":
        "kill $(pgrep -f '{chip_tool} interactive start')",
    "READ_SUBSCRIBE_CLUSTER_ATTRIBUTE_OUTPUT":
        "grep 'Data =' {logging_file_path}",
    "SEND_CLUSTER_COMMMAND":
        "{chip_tool} {cluster} {command} {arguments} {node_id} {endpoint_id} "
        "{flags}",
    "COMMISSION_OVER_BLE_WIFI":
        "{chip_tool} pairing ble-wifi {node_id} {ssid} {password} {setup_code} "
        "{long_discriminator}",
    "COMMISSION_OVER_BLE_THREAD":
        "{chip_tool} pairing ble-thread {node_id} {operational_dataset} "
        "{setup_code} {long_discriminator}",
    "COMMISSION_ON_NETWORK":
        "{chip_tool} pairing onnetwork {node_id} {setup_code}",
    "COMMISSION_ON_NETWORK_LONG":
        "{chip_tool} pairing onnetwork-long {node_id} {setup_code} "
        "{long_discriminator}",
    "DECOMMISSION":
        "{chip_tool} pairing unpair {node_id}",
    "CHIP_TOOL_VERSION":
        "cat ~/.matter_sdk_version",
    "WRITE_CHIP_TOOL_VERSION":
        "echo {chip_tool_version} > ~/.matter_sdk_version",
    "CLEAR_TEMP_DIRECTORY":
        "rm -rf /tmp/chip*",
    "CLEAR_STORAGE":
        "{chip_tool} storage clear-all",
    "MAKE_CERTS_DIRECTORY":
        "mkdir -p {rpi_certs_dir}",
    "MOVE_CERTS_TO_CERTS_DIRECTORY":
        "mv {rpi_temp_certs_dir} {rpi_certs_dest}",
})

_REGEXES = immutabledict.immutabledict({
    "READ_CLUSTER_ATTRIBUTE_RESPONSE":
        r'Data = ([a-zA-Z0-9_+.-]+|".*")',
    "WRITE_CLUSTER_ATTRIBUTE_RESPONSE":
        r"CHIP:DMG:\s+status = (0[xX][0-9a-fA-F]+)",
    "SUBSCRIBE_CLUSTER_ATTRIBUTE_RESPONSE":
        r'Data = ([a-zA-Z0-9_+.-]+|".*")',
    "SEND_CLUSTER_COMMAND_RESPONSE":
        r"Received Command Response Status for Endpoint=\d+ "
        r"Cluster=0[xX][0-9a-fA-F_]+ Command=0[xX][0-9a-fA-F_]+ "
        r"Status=(0[xX][0-9a-fA-F]+)",
    "COMMAND_FAILURE":
        r"Run command failure: (.*)",
    "COMMISSION_SUCCESS":
        "(CHIP:TOO: Device commissioning completed with success)",
    "DECOMMISSION_COMPLETE":
        "(CHIP:DL: System Layer shutdown)",
})

_TIMEOUTS = immutabledict.immutabledict({
    "COMMISSION": 60,
    "SEND_CLUSTER_COMMAND": 30,
})


def _str_to_hex(value: str) -> str:
  """Formats a string into chip-tool compatible CLI argument.

  If the string starts with "hex:" prefix, then this function
  returns the value as is. Otherwise, the string is converted
  into its two-digit hex numbers form and prefixed with "hex:".
  For example, "password" is converted to "hex:70617373776f7264".

  See
  https://github.com/project-chip/connectedhomeip/tree/master/examples/chip-tool#using-the-client-to-commission-a-device
  for example usage.

  Args:
    value: The string to be converted.

  Returns:
    Value in its two-digit hex numbers form with "hex:" prefix.
  """
  if value.startswith(_HEX_PREFIX):
    return value

  hex_str = binascii.hexlify(str.encode(value))
  return f"{_HEX_PREFIX}{hex_str.decode()}"


def _list_certs(url: str) -> requests.Response:
  try:
    certs_list = http_utils.send_http_get(url)
  except RuntimeError as e:
    raise errors.DeviceError(
        f"Error listing files from Matter SDK({url}) "
    ) from e
  return certs_list


def _parse_response(response: str) -> Any:
  try:
    return ast.literal_eval(response)
  except ValueError:
    if response.lower() in ["true", "false"]:
      return response.lower() == "true"
    raise


class MatterControllerChipTool(matter_controller_base.MatterControllerBase):
  """Matter controller capability using chip-tool CLI commands."""

  def __init__(self,
               device_name: str,
               shell_fn: Callable[..., str],
               regex_shell_fn: Callable[..., str],
               send_file_to_device: Callable[[str, str], None],
               set_property_fn: Callable[..., None],
               get_property_fn: Callable[..., Any],
               chip_tool_path: str = _CHIP_TOOL_BINARY_PATH):
    """Creates an instance of MatterControllerChipTool capability.

    Args:
      device_name: Name of the device this capability is attached to.
      shell_fn: Bound 'shell' method of the device class instance.
      regex_shell_fn: Bound 'shell_with_regex' method of the device class
        instance.
      send_file_to_device: Bound 'send_file_to_device' method of the device's
        file transfer capability instance.
      set_property_fn: Bound 'set_property' method of the Manager instance.
      get_property_fn: Bound 'get_property' method of the Manager instance.
      chip_tool_path: Path to chip-tool binary on the device.
    """
    super().__init__(device_name)

    self._chip_tool_path = chip_tool_path
    self._shell_with_regex = regex_shell_fn
    self._shell = shell_fn
    self._send_file_to_device = send_file_to_device
    self._get_property_fn = get_property_fn
    self._set_property_fn = set_property_fn

  @decorators.DynamicProperty
  def version(self) -> str:
    """Matter SDK version of the controller."""
    return self._shell(_COMMANDS["CHIP_TOOL_VERSION"])

  @decorators.DynamicProperty
  def path(self) -> str:
    """Path to chip-tool binary."""
    return self._chip_tool_path

  @decorators.CapabilityLogDecorator(logger)
  def commission(self,
                 node_id: int,
                 setup_code: str,
                 long_discriminator: Optional[int] = None,
                 ssid: Optional[str] = None,
                 password: Optional[str] = None,
                 operational_dataset: Optional[str] = None,
                 paa_trust_store_path: Optional[str] = None) -> None:
    """Commissions a device into the controller's fabric.

    Commissioning protocol is based on specified arguments:
      - When operational dataset is provided, pairs the device over ble-thread.
      - When Wi-Fi SSID and password are provided, pairs the device over
        ble-wifi.
      - Otherwise, discover the devices on the network and pairs with the first
        one that matches the setup code and long discriminator if one is
        specified.

    Args:
      node_id: Node ID to assign to the node being commissioned.
      setup_code: Set up PIN code of the remote device.
      long_discriminator: Discriminator of the remote device.
      ssid: Wi-Fi SSID either as a string, or in the form hex:XXXXXXXX where the
        bytes of the SSID are encoded as two-digit hex numbers.
      password: Wi-Fi password, either as a string or as hex data.
      operational_dataset: Thread dataset in base-64. This argument is mutually
        exclusive with ssid and password.
      paa_trust_store_path: Path to directory holding PAA cert information
        on the controller device (e.g. rpi_matter_controller). See
        https://github.com/project-chip/connectedhomeip/tree/master/credentials/development/paa-root-certs # pylint: disable=line-too-long
        for an example.
    """
    if ssid and not password:
      raise ValueError("Wi-Fi password is not specified.")

    if operational_dataset:
      command = _COMMANDS["COMMISSION_OVER_BLE_THREAD"]
      operational_dataset = f"{_HEX_PREFIX}{operational_dataset}"
    elif ssid:
      command = _COMMANDS["COMMISSION_OVER_BLE_WIFI"]
      ssid = _str_to_hex(ssid)
      password = _str_to_hex(password)
    elif long_discriminator is not None:
      # Commission the first device found on the network with provided
      # setup code and long discriminator.
      command = _COMMANDS["COMMISSION_ON_NETWORK_LONG"]
    else:
      # Commission the first device found on the network with provided
      # setup code.
      command = _COMMANDS["COMMISSION_ON_NETWORK"]

    if paa_trust_store_path is not None:
      command += f" --paa-trust-store-path {paa_trust_store_path}"

    command = command.format(
        chip_tool=self._chip_tool_path,
        node_id=node_id,
        setup_code=setup_code,
        long_discriminator=long_discriminator,
        ssid=ssid,
        password=password,
        operational_dataset=operational_dataset,
    )
    self._shell_with_regex(
        command,
        _REGEXES["COMMISSION_SUCCESS"],
        raise_error=True,
        timeout=_TIMEOUTS["COMMISSION"])

    self._set_property_fn(_MATTER_NODE_ID_PROPERTY, node_id)

  @decorators.CapabilityLogDecorator(logger)
  def decommission(self) -> None:
    """Forgets a commissioned device with the given node id."""
    command = _COMMANDS["DECOMMISSION"].format(
        chip_tool=self._chip_tool_path,
        node_id=self._get_property_fn(_MATTER_NODE_ID_PROPERTY))
    self._shell_with_regex(
        command, _REGEXES["DECOMMISSION_COMPLETE"], raise_error=True)
    self._set_property_fn(_MATTER_NODE_ID_PROPERTY, None)

  def read(self, endpoint_id: int, cluster: str, attribute: str) -> Any:
    """Reads a cluster's attribute for the given node id and endpoint.

    Only primitive attribute values (integer, float, boolean and string)
    are supported.

    Args:
      endpoint_id: Endpoint ID within the node to read attribute from.
      cluster: Name of the cluster to read the attribute value from.
      attribute: Name of the cluster attribute to read.

    Returns:
      Attribute value of the cluster.
    """
    command = _COMMANDS["READ_CLUSTER_ATTRIBUTE"].format(
        chip_tool=self._chip_tool_path,
        node_id=self._get_property_fn(_MATTER_NODE_ID_PROPERTY),
        endpoint_id=endpoint_id,
        cluster=cluster,
        attribute=attribute,
    )
    response = self._shell_with_regex(
        command, _REGEXES["READ_CLUSTER_ATTRIBUTE_RESPONSE"], raise_error=True)

    return _parse_response(response)

  @decorators.CapabilityLogDecorator(logger)
  def write(self, endpoint_id: int, cluster: str, attribute: str,
            value: Any) -> None:
    """Writes a cluster's attribute for the given node id and endpoint.

    Args:
      endpoint_id: Endpoint ID within the node to write attribute to.
      cluster: Name of the cluster to write the attribute value to (e.g. onoff).
      attribute: Name of the cluster attribute to write (e.g. on-time).
      value: New attribute value to update the cluster with.
    """
    command = _COMMANDS["WRITE_CLUSTER_ATTRIBUTE"].format(
        chip_tool=self._chip_tool_path,
        node_id=self._get_property_fn(_MATTER_NODE_ID_PROPERTY),
        endpoint_id=endpoint_id,
        cluster=cluster,
        attribute=attribute,
        value=value,
    )
    status_code = self._shell_with_regex(
        command, _REGEXES["WRITE_CLUSTER_ATTRIBUTE_RESPONSE"], raise_error=True)
    if int(status_code, 0) != 0:
      raise errors.DeviceError(
          f"{self._device_name} '{command}' responded with a non-zero "
          f"status code: {status_code}")

  @decorators.CapabilityLogDecorator(logger)
  def start_subscription(self, endpoint_id: int, cluster: str, attribute: str,
                         min_interval_s: int, max_interval_s: int) -> None:
    """Starts a subscription to a cluster's attribute.

    Args:
      endpoint_id: Endpoint ID within the node to write attribute to.
      cluster: Name of the cluster to write the attribute value to (e.g. onoff).
      attribute: Name of the cluster attribute to write (e.g. on-time).
      min_interval_s: Server should not send a new report if less than this
        number of seconds has elapsed since the last report.
      max_interval_s: Server must send a report if this number of seconds has
        elapsed since the last report.
    """
    command = _COMMANDS["SUBSCRIBE_CLUSTER_ATTRIBUTE_START"].format(
        chip_tool=self._chip_tool_path,
        node_id=self._get_property_fn(_MATTER_NODE_ID_PROPERTY),
        endpoint_id=endpoint_id,
        cluster=cluster,
        attribute=attribute,
        min_interval_s=min_interval_s,
        max_interval_s=max_interval_s,
        logging_file_path=LOGGING_FILE_PATH,
    )
    self._shell(command)

  @decorators.CapabilityLogDecorator(logger)
  def stop_subscription(self) -> List[Any]:
    """Stops existing subscription and returns subscribed values.

    Returns:
      List of attribute values.
    """
    self._shell(_COMMANDS["SUBSCRIBE_CLUSTER_ATTRIBUTE_STOP"].format(
        chip_tool=self._chip_tool_path))

    command = _COMMANDS["READ_SUBSCRIBE_CLUSTER_ATTRIBUTE_OUTPUT"].format(
        logging_file_path=LOGGING_FILE_PATH)
    responses = re.findall(_REGEXES["SUBSCRIBE_CLUSTER_ATTRIBUTE_RESPONSE"],
                           self._shell(command))
    return [_parse_response(response) for response in responses]

  @decorators.CapabilityLogDecorator(logger)
  def subscribe(self,
                endpoint_id: int,
                cluster: str,
                attribute: str,
                min_interval_s: int,
                max_interval_s: int,
                timeout_s: int = 10) -> List[Any]:
    """Subscribes to a cluster's attribute and blocks until timeout.

    Args:
      endpoint_id: Endpoint ID within the node to write attribute to.
      cluster: Name of the cluster to write the attribute value to (e.g. onoff).
      attribute: Name of the cluster attribute to write (e.g. on-time).
      min_interval_s: Server should not send a new report if less than this
        number of seconds has elapsed since the last report.
      max_interval_s: Server must send a report if this number of seconds has
        elapsed since the last report.
      timeout_s: Number of seconds to subscribe to this attribute for.

    Returns:
      List of attribute values.
    """
    self.start_subscription(endpoint_id, cluster, attribute, min_interval_s,
                            max_interval_s)
    time.sleep(timeout_s)
    return self.stop_subscription()

  @decorators.CapabilityLogDecorator(logger)
  def send(self,
           endpoint_id: int,
           cluster: str,
           command: str,
           arguments: Sequence[Any],
           flags: Optional[Sequence[Any]] = None) -> None:
    """Sends a command to a device with the given node id and endpoint.

    Args:
      endpoint_id: Endpoint ID within the node to read attribute from.
      cluster: Name of the cluster to send the command to (e.g. onoff).
      command: Name of the command to send (e.g. toggle).
      arguments: Command arguments.
      flags: Additional flags passed to chip-tool send command. None if it's not
        provided.
    """
    additional_flags = "" if flags is None else " ".join(map(str, flags))
    command = _COMMANDS["SEND_CLUSTER_COMMMAND"].format(
        chip_tool=self._chip_tool_path,
        node_id=self._get_property_fn(_MATTER_NODE_ID_PROPERTY),
        endpoint_id=endpoint_id,
        cluster=cluster,
        command=command,
        arguments=" ".join(map(str, arguments)),
        flags=additional_flags,
    )
    command = command.rstrip()
    status_code = self._shell_with_regex(
        command,
        _REGEXES["SEND_CLUSTER_COMMAND_RESPONSE"],
        raise_error=True,
        timeout=_TIMEOUTS["SEND_CLUSTER_COMMAND"])
    if int(status_code, 0) != 0:
      raise errors.DeviceError(
          f"{self._device_name} '{command}' responded with a non-zero "
          f"status code: {status_code}")

  @decorators.CapabilityLogDecorator(logger)
  def upgrade(self, build_file: str, build_id: str,
              paa_trust_store_path: str = DEFAULT_PAA_TRUST_STORE_PATH) -> None:
    """Installs chip-tool binary to the controller device and downloads matter certs.

    Args:
      build_file: Path to chip-tool binary on the host machine.
      build_id: Commit SHA the chip-tool binary is built at.
      paa_trust_store_path: Path where matter certs will be downloaded.
    """
    self._send_file_to_device(build_file, self._chip_tool_path)
    self._shell(
        _COMMANDS["WRITE_CHIP_TOOL_VERSION"].format(chip_tool_version=build_id))
    self.update_certs(paa_trust_store_path)

  @decorators.CapabilityLogDecorator(logger)
  def factory_reset(self) -> None:
    """Factory resets all settings stored on controller's device."""
    self._shell(_COMMANDS["CLEAR_TEMP_DIRECTORY"])
    self._shell(_COMMANDS["CLEAR_STORAGE"].format(
        chip_tool=self._chip_tool_path))

  @decorators.CapabilityLogDecorator(logger)
  def update_certs(self,
                   device_dest: str,
                   host_dest: Optional[str] = None) -> None:
    """Downloads certs from Matter SDK and to the device.

    Downloads certs and stores in the specified path in the host. Later, copies
    them to the specified path in the device.

    Args:
      device_dest: Directory path in the device to which the certs will be
        copied from the host machine.
      host_dest: Directory path in the host machine to store the certs. If not
        specified, a temporary directory will be used and cleaned up before
        exit.
    """

    with tempfile.TemporaryDirectory(prefix="chip_tool_") as tmp_dir:
      commit_sha = http_utils.send_http_get(
          _MATTER_SDK_REPO,
          headers={"Accept": "application/vnd.github.VERSION.sha"}).content
      logger.info(
          f"{self._device_name} Downloading certs from Matter SDK with commit SHA: {commit_sha.decode()}"
      )
      certs_list = _list_certs(_MATTER_SDK_CERTS_DIRECTORY_PATH).json()
      for cert in certs_list:
        response = http_utils.send_http_get(cert["download_url"])
        with open(os.path.join(tmp_dir, cert["name"]), "wb") as file:
          file.write(response.content)

      self._shell(_COMMANDS["MAKE_CERTS_DIRECTORY"].format(
          rpi_certs_dir=_RPI_TEMP_CERTS_DIR,
      ))
      self._send_file_to_device(tmp_dir, _RPI_TEMP_CERTS_DIR)
      self._shell(_COMMANDS["MAKE_CERTS_DIRECTORY"].format(
          rpi_certs_dir=device_dest,
      ))
      self._shell(_COMMANDS["MOVE_CERTS_TO_CERTS_DIRECTORY"].format(
          rpi_temp_certs_dir=os.path.join(
              _RPI_TEMP_CERTS_DIR, os.path.basename(tmp_dir), "*"),
          rpi_certs_dest=device_dest,
      ))
      if host_dest is not None:
        shutil.copytree(tmp_dir, host_dest, dirs_exist_ok=True)
