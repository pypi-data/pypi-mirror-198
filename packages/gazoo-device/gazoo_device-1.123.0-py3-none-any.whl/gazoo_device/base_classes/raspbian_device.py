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

"""Base class for all raspbian devices."""
import re
import time
from typing import Callable, List

from gazoo_device import config
from gazoo_device import console_config
from gazoo_device import decorators
from gazoo_device import errors
from gazoo_device import gdm_logger
from gazoo_device.base_classes import auxiliary_device
from gazoo_device.capabilities import file_transfer_scp
from gazoo_device.capabilities import shell_ssh
from gazoo_device.switchboard import switchboard
from gazoo_device.utility import deprecation_utils
from gazoo_device.utility import host_utils

logger = gdm_logger.get_logger()

_MARKER = "--- GDM Log Marker ---"
_LOGGING_FILE_PATH = "/var/log/syslog"
_LOG_MARKER_LINE_POS_OR_EMPTY = (
    'grep -n -e "{marker}" {file_path} --text | tail -n 1 | cut -d '
    '":" -f 1').format(
        marker=_MARKER, file_path=_LOGGING_FILE_PATH)
_LOG_MARKER_LINE_POS = (
    "line_num=$({cmd}); [ -z \"$line_num\" ] && echo 1 || echo"
    " $line_num".format(cmd=_LOG_MARKER_LINE_POS_OR_EMPTY))

COMMANDS = {
    "BOOTUP_COMPLETE":
        "sudo systemctl --wait is-system-running",
    "FIRMWARE_VERSION":
        "cat /etc/os-release",
    "INJECT_LOG_MARKER":
        "sudo bash -c 'echo \"{marker}\" >> {file_path}'".format(
            marker=_MARKER, file_path=_LOGGING_FILE_PATH),
    "KERNEL_VERSION":
        "uname -r",
    "LOGGING":
        ("tail", "-F", "-n", f"+$({_LOG_MARKER_LINE_POS})", _LOGGING_FILE_PATH),
    "MODEL_INFO":
        "cat /proc/device-tree/model",
    "GDM_HELLO":
        "echo 'GDM-HELLO'",
    "REBOOT":
        "sudo reboot",
    "RESET_FAILED":
        "sudo systemctl reset-failed",
    "SERIAL_NUMBER_INFO":
        "cat /proc/cpuinfo",
}

REGEXES = {
    "COMMAND_UNSUPPORTED": r"-bash: \S+: command not found",
    "device_type": "raspberrypi",
    "FIRMWARE_VERSION_REGEX": r"VERSION=\"(\d+ \(\w+\))\"",
    "KERNEL_VERSION_REGEX": r"(.*)",
    "MODEL_INFO_REGEX": r"Raspberry Pi ([^\n]+)",
    "SERIAL_NUMBER_INFO_REGEX": r"Serial\s+: ([^\n]+)"
}

TIMEOUTS = {"GDM_HELLO": 5, "SHELL": 10, "SHUTDOWN": 60, "ONLINE": 120}


class RaspbianDevice(auxiliary_device.AuxiliaryDevice):
  """Base Class for Raspbian Devices."""
  COMMUNICATION_TYPE = "SshComms"
  _COMMUNICATION_KWARGS = {
      "log_cmd": COMMANDS["LOGGING"],
      "key_info": config.KEYS["raspberrypi3_ssh_key"],
      "username": "pi"
  }

  def __init__(self,
               manager,
               device_config,
               log_file_name=None,
               log_directory=None):
    super().__init__(
        manager,
        device_config,
        log_file_name=log_file_name,
        log_directory=log_directory)
    self._commands.update(COMMANDS)
    self._regexes.update(REGEXES)
    self._timeouts.update(TIMEOUTS)

  @decorators.health_check
  def check_device_responsiveness(self):
    """Check if the device is responsive on console.

    Raises:
        DeviceNotResponsiveError: if device is not responsive on console.
    """
    cmd, timeout = self.commands["GDM_HELLO"], self.timeouts["GDM_HELLO"]
    try:
      self.shell(cmd, timeout=timeout)
    except errors.DeviceError as err:
      raise errors.DeviceNotResponsiveError(
          self.name,
          "unable to execute command {!r} on device's shell".format(cmd),
          timeout=timeout,
          details=str(err))

  @decorators.DynamicProperty
  def kernel_version(self):
    """Version of Raspbian kernel.

    Returns:
        str: Raspbian kernel version.
    """
    return self.shell_with_regex(
        self.commands["KERNEL_VERSION"],
        self.regexes["KERNEL_VERSION_REGEX"],
        raise_error=True)

  @decorators.DynamicProperty
  def firmware_version(self):
    """Version of Raspbian.

    Returns:
        str: Raspbian version.
    """
    return self.shell_with_regex(
        self.commands["FIRMWARE_VERSION"],
        self.regexes["FIRMWARE_VERSION_REGEX"],
        raise_error=True)

  @decorators.PersistentProperty
  def platform(self) -> str:
    """Returns the platform type of the device."""
    return "Raspbian"

  def get_console_configuration(self) -> console_config.ConsoleConfiguration:
    """Returns the interactive console configuration."""
    return console_config.get_log_response_separate_port_configuration(
        self.switchboard.get_line_identifier())

  @decorators.PersistentProperty
  def health_checks(self) -> List[Callable[[], None]]:
    """Returns list of methods to execute as health checks."""
    return [
        self.check_device_connected, self.check_create_switchboard,
        self.check_device_responsiveness
    ]

  @decorators.PersistentProperty
  def ip_address(self):
    """Global IP address."""
    return self.communication_address

  @decorators.CapabilityDecorator(shell_ssh.ShellSSH)
  def shell_capability(self):
    return self.lazy_init(
        shell_ssh.ShellSSH,
        self.switchboard.send_and_expect,
        self.name,
        timeout=self.timeouts["SHELL"],
        tries=2)

  @decorators.CapabilityDecorator(file_transfer_scp.FileTransferScp)
  def file_transfer(self):
    """File transfer capability for moving files from and to the device.

    Returns:
        FileTransferScp: file transfer capability using "scp" command.
    """
    return self.lazy_init(
        file_transfer_scp.FileTransferScp,
        ip_address_or_fn=self.ip_address,
        device_name=self.name,
        add_log_note_fn=self.switchboard.add_log_note,
        user=self._COMMUNICATION_KWARGS["username"],
        key_info=self._COMMUNICATION_KWARGS["key_info"])

  @decorators.LogDecorator(logger)
  def recover(self, error):
    """Recovers the device from an error detected by check_device_ready()."""
    if isinstance(error, errors.DeviceNotResponsiveError):
      self.reboot()
    else:
      raise error

  @decorators.LogDecorator(logger)
  def reboot(self, no_wait=False, method="shell"):
    """Reboots the device.

    Verifies device fully boots up afterwards.

    Args:
        no_wait (bool): Return before reboot completes. Default: False
        method (str): reboot technique to use.
    """
    self._inject_log_marker()
    self.switchboard.add_log_note("GDM triggered reboot")
    self.switchboard.send(command=self.commands["REBOOT"])
    if not no_wait:
      self._verify_reboot()

  @decorators.LogDecorator(logger)
  def get_detection_info(self):
    """Gets the persistent and optional attributes of a device during setup.

    Returns:
      tuple: (dict, dict) dictionary of persistent attributes,
              dictionary of optional attributes (set to None).
    """
    self.props = self.props.copy()
    for cmd_name, command in self.commands.items():
      if not cmd_name.endswith("INFO"):
        continue
      regex = self._regexes[cmd_name + "_REGEX"]
      cmd_name = cmd_name.lower()[:-5]  # remove _INFO
      value = self.shell_with_regex(command, regex)
      if re.search(self.regexes["COMMAND_UNSUPPORTED"], value):
        value = "Raspbian detection did not support '{}'".format(command)
      self.props["persistent_identifiers"][cmd_name] = value

    return self.props["persistent_identifiers"], self.props["optional"]

  @classmethod
  def is_connected(cls, device_config):
    """Checks whether or not the device is connected to the computer.

    Args:
        device_config (dict): contains "persistent" dict

    Returns:
        bool: True if device is pingable, False otherwise.

    Notes:
        device_config is typically the device_config from manager.
        It checks if the device is reachable or not.
    """
    ip_address = device_config["persistent"]["console_port_name"]
    return host_utils.is_pingable(ip_address)

  def shell(self,
            command,
            command_name="shell",
            timeout=None,
            port=0,
            include_return_code=False,
            searchwindowsize=config.SEARCHWINDOWSIZE):
    """Sends command and returns response and optionally return code.

    Args:
        command(str): Command to send to the device.
        command_name(str): Identifier for command.
        timeout(float): Time in seconds to wait for device to respond.
        port(int): Which port to send on. Port 0 is typically used for commands.
        include_return_code(bool): Whether to also return the command
          return code.
        searchwindowsize(int): Number of the last bytes to look at.

    Raises:
        DeviceError: if communication fails.

    Note:
        Can try multiple times as connection can sometimes fail.
        See shell_capability init args for setting the number of retry
        attempts.

    Returns:
        str: If include_return_code is False return the device response to
        the command.
        tuple: If include_return_code is True return the device response and
        return code.
    """
    timeout = timeout or self.timeouts["SHELL"]
    return self.shell_capability.shell(
        command,
        command_name=command_name,
        timeout=timeout,
        port=port,
        include_return_code=include_return_code,
        searchwindowsize=searchwindowsize)

  def shell_with_regex(self,
                       command,
                       regex,
                       regex_group=1,
                       command_name="shell",
                       raise_error=False,
                       tries=1,
                       port=0,
                       timeout=None,
                       searchwindowsize=config.SEARCHWINDOWSIZE):
    """Sends a command, searches for a regex in the response, and returns a match group.

    Args:
        command(str): command to issue.
        regex(str): regular expression with one or more capturing groups.
        regex_group(int): number of regex group to return.
        command_name(str): command name to appear in log messages.
        raise_error(bool): whether or not to raise error if unable to find a
          match.
        tries(int): how many times to try executing the command before
          failing.
        port(int): which port to send the shell command to.
        timeout(float): Time in seconds to wait for device to respond.
        searchwindowsize(int): Number of the last bytes to look at

    Returns:
        str: value of the capturing group with index 'regex_group' in the
        match.

    Raises:
        DeviceError: if command execution fails OR
                     couldn't find the requested group in any of the
                     responses.
    """
    return self.command_with_regex(
        command,
        regex,
        self.shell,
        regex_group=regex_group,
        raise_error=raise_error,
        tries=tries,
        command_name=command_name,
        port=port,
        timeout=timeout)

  @decorators.CapabilityDecorator(switchboard.SwitchboardDefault)
  def switchboard(self):
    """Instance for communicating with the device."""
    switchboard_name = self._get_private_capability_name(
        switchboard.SwitchboardDefault)
    if not hasattr(self, switchboard_name):
      switchboard_kwargs = self._COMMUNICATION_KWARGS.copy()
      switchboard_kwargs.update({
          "communication_address": self.communication_address,
          "communication_type": self.COMMUNICATION_TYPE,
          "log_path": self.log_file_name,
          "device_name": self.name,
          "event_parser": None})
      setattr(self, switchboard_name,
              self.get_manager().create_switchboard(**switchboard_kwargs))

    return getattr(self, switchboard_name)

  def _ensure_device_goes_offline(self, timeout=None):
    """Ensure device is no longer pingable over ssh.

    Args:
        timeout(float): Time in seconds to wait for device to respond.

    Raises:
        DeviceError: Deviced failed to go offline before the timeout
    """
    timeout = timeout or self.timeouts["SHUTDOWN"]
    start_time = time.time()
    max_disconnect_time = start_time + timeout
    count = 0
    while time.time() < max_disconnect_time:
      if not host_utils.is_pingable(self.ip_address):
        count += 1  # Ensure device is really offline not just a blip
      else:
        count = 0
      if count == 2:
        logger.info("{} offline in {}s.".format(self.name,
                                                int(time.time() - start_time)))
        # close ssh transport as the ssh connection is disconnected.
        self.switchboard.close_all_transports()
        time.sleep(5)  # to ensure offline
        return
      time.sleep(.5)

    raise errors.DeviceError("Failed to go offline within {}s.".format(timeout))

  def _inject_log_marker(self):
    """Add GDM log marker to / var / log / syslog.

    This is to prevent reading stale logs.

    Note:
        Device logs are read starting with the last log marker(if present).
    """
    self.shell(self.commands["INJECT_LOG_MARKER"])

  def _ensure_device_is_online(self, timeout=None):
    """Ensure device is online and configs are fully loaded.

    Args:
        timeout(float): Time in seconds to wait for device to respond.

    Raises:
        DeviceError: Device failed to come online before the timeout.
    """
    timeout = timeout or self.timeouts["ONLINE"]

    start_time = time.time()
    max_disconnect_time = start_time + timeout
    try:
      self.wait_until_connected(timeout=timeout)
    except errors.DeviceNotConnectedError as error:
      raise errors.DeviceNotBootupCompleteError(
          self.name,
          f"boot up failed. Device failed to become pingable in {timeout}s"
      ) from error

    # There's a delay between the device being responsive to ping and being able
    # to open SSH connections
    time.sleep(10)
    self.switchboard.open_all_transports()

    output = "Device still offline"
    while time.time() < max_disconnect_time:
      # Ensure the BOOTUP_COMPLETE command is only sent once
      boot_up_complete_timeout = max_disconnect_time - time.time()
      try:
        output, return_code = self.shell(
            self.commands["BOOTUP_COMPLETE"],
            timeout=boot_up_complete_timeout,
            include_return_code=True)
        if return_code == 0:  # command executed
          logger.info("{} online in {}s".format(self.name,
                                                int(time.time() - start_time)))
          return
        self.shell(self.commands["RESET_FAILED"])
      except errors.DeviceError:
        logger.debug(
            "{} failed to respond to {!r}.".format(
                self.name, self.commands["BOOTUP_COMPLETE"]),
            exc_info=True)
      time.sleep(.5)
    raise errors.DeviceError(
        "Failed to come online and respond to {!r} in {}s. Response: {}".format(
            self.commands["BOOTUP_COMPLETE"], timeout, output))

  def _verify_reboot(self):
    """Verifies reboot actually occurred."""
    self._ensure_device_goes_offline()
    self._ensure_device_is_online()

  def _list_properties_dynamic_raspbian(self):
    dyn_list = ["firmware_version", "kernel_version"]
    return set(dyn_list)


deprecation_utils.add_deprecated_attributes(
    RaspbianDevice,
    [("send_file_to_device", "file_transfer.send_file_to_device", True),
     ("recv_file_from_device", "file_transfer.recv_file_from_device", True),
     ("do_and_expect", "switchboard.do_and_expect", True),
     ("expect", "switchboard.expect", True),
     ("send", "switchboard.send", True),
     ("send_and_expect", "switchboard.send_and_expect", True)])
