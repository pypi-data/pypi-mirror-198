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

"""Abstract base class containing required GDM APIs for auxiliary devices.

Some of these APIs are implemented in AuxiliaryDevice and don't need to be
re-implemented in derived device classes. Device classes should inherit from
AuxiliaryDevice, not from this class.
"""
import abc
from typing import Callable, List, Optional

from gazoo_device import console_config
from gazoo_device import data_types


class AuxiliaryDeviceBase(abc.ABC):
  """Abstract base class containing required GDM APIs for auxiliary devices."""
  COMMUNICATION_TYPE = None  # Override
  DETECT_MATCH_CRITERIA = None  # Overrride
  DEVICE_TYPE = None  # Override
  _COMMUNICATION_KWARGS = {}
  _OWNER_EMAIL = ""  # override in child classes
  # Maximum number of attempts for recovery from health check failures.
  _RECOVERY_ATTEMPTS = 1

  @abc.abstractproperty
  def alias(self):
    """Returns the user-defined device alias (string)."""

  @abc.abstractproperty
  def commands(self):
    """Dictionary of commands issued to the device via shell."""

  @abc.abstractproperty
  def communication_address(self):
    """Returns the name of the main communication port (for example, ip address)."""

  @abc.abstractproperty
  def connected(self):
    """Returns whether the device is connected or not."""

  @abc.abstractmethod
  def get_console_configuration(
      self) -> Optional[console_config.ConsoleConfiguration]:
    """Returns interactive console configuration or None if not supported."""

  @abc.abstractproperty
  def health_checks(self) -> List[Callable[[], None]]:
    """Returns list of methods to execute as health checks."""

  @abc.abstractproperty
  def model(self):
    """Returns the device model."""

  @abc.abstractproperty
  def name(self):
    """Returns the unique identifier for the device (like cambrionix-a3b4)."""

  @abc.abstractproperty
  def regexes(self):
    """Regular expressions used to retrieve properties, events, states from device output."""

  @abc.abstractproperty
  def serial_number(self):
    """Returns the serial number of the device."""

  @abc.abstractproperty
  def timeouts(self):
    """Dictionary of default timeouts to use when expecting certain actions."""

  @abc.abstractmethod
  def check_device_ready(self):
    """Checks if the device is ready for testing.

    If not, raises a CheckDeviceReadyError.

    This is typically implemented by checking if device responds to shell
    commands and if it's streaming logs. There can be additional device-specific
    checks as well.
    """

  @abc.abstractmethod
  def close(self, force: bool = False):
    """Releases all resources if there are no more instance users.

    If there is at least one other instance user, does not close the device and
    only decrements user count.

    Args:
      force: If True, ignore the active user count and close the device even if
        there are remaining users.
    """

  @abc.abstractmethod
  def get_detection_info(self):
    """Gets the persistent and optional attributes of a device during setup.

    Returns:
      tuple: (dict, dict) dictionary of persistent attributes,
              dictionary of optional attributes (set to None).
    """

  @abc.abstractmethod
  def get_dynamic_properties(self):
    """Returns dictionary of dynamic properties."""

  @abc.abstractmethod
  def get_optional_properties(self):
    """Returns dictionary of optional properties."""

  @abc.abstractmethod
  def get_persistent_properties(self):
    """Returns dictionary of persistent properties."""

  @abc.abstractmethod
  def get_property_names(self):
    """Returns a list of all property names."""

  @abc.abstractmethod
  def is_connected(cls, device_config):  # pylint: disable=no-self-argument
    """Determines if the device is connected (reachable).

    Note:
        This method is used during device detection.
        This should be a class or static method, not an instance method.

    Args:
        device_config (dict): contains "persistent" dict

    Returns:
        bool: True if the device is connected (i.e. pingable), False
        otherwise.
    """

  @abc.abstractmethod
  def make_device_ready(
      self, setting: data_types.MakeDeviceReadySettingStr = "on") -> None:
    """Checks device readiness and attempts recovery if allowed.

    If setting is 'off': does nothing.
    If setting is 'check_only': only checks readiness (recovery is skipped).
    If setting is 'on': checks readiness and attempts recovery
    self._RECOVERY_ATTEMPTS times.
    If setting is 'flash_build': same as 'on', but will attempt reflashing the
    device if it's supported and if all other recovery methods fail.

    Args:
      setting: 'on', 'off', 'check_only', or 'flash_build'.

    Raises:
      CheckDeviceReadyError: Re-raises the device readiness check error if
        unable to recover from it.
      DeviceError: If the recovery process raises an error.
    """

  @abc.abstractmethod
  def recover(self, error):
    """Attempts to recover device based on the type of error specified.

    Note: The check_device_ready method can raise a number of separate
    exceptions which are passed to this method as exception objects. The
    recovery method is chosen based on the type of the error. See subclasses of
    CheckDeviceError in errors.py for a list of errors raised by
    check_device_ready.

    Args:
        error (CheckDeviceReadyError): A subclass of CheckDeviceReadyError
        that will be used to identify a possible recovery solution to use.

    Raises:
        DeviceError: If device recovery fails while attempting to perform
        recovery steps.
        CheckDeviceReadyError: If there are no recovery steps available for
        the error argument, it will be re-raised directly.
    """

  @abc.abstractmethod
  def wait_until_connected(self, timeout: Optional[int] = None) -> None:
    """Wait until the device is connected to the host.

    Args:
        timeout: Max time to wait for the device to be reachable from the host.

    Raises:
        DeviceNotConnectedError: device did not become reachable from the host
            before the timeout was exceeded.
    """
