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

"""Raspberry Pi Matter Controller device class."""

from typing import Optional

from gazoo_device import config
from gazoo_device import decorators
from gazoo_device import detect_criteria
from gazoo_device import errors
from gazoo_device import gdm_logger
from gazoo_device.auxiliary_devices import raspberry_pi
from gazoo_device.base_classes import matter_endpoints_mixin
from gazoo_device.capabilities import matter_controller_chip_tool
from gazoo_device.capabilities import matter_endpoints_accessor_chip_tool

logger = gdm_logger.get_logger()

_LOGGING_CMD = ("tail", "-F", matter_controller_chip_tool.LOGGING_FILE_PATH)


class RaspberryPiMatterController(
    raspberry_pi.RaspberryPi,
    matter_endpoints_mixin.MatterEndpointAliasesMixin):
  """Base Class for RaspberryPiMatterController Devices."""
  _COMMUNICATION_KWARGS = {
      "log_cmd": _LOGGING_CMD,
      "key_info": config.KEYS["raspberrypi3_ssh_key"],
      "username": "pi"
  }
  DETECT_MATCH_CRITERIA = {
      detect_criteria.SshQuery.IS_RASPBIAN_RPI: True,
      detect_criteria.SshQuery.IS_CHIP_TOOL_PRESENT: True,
  }
  DEVICE_TYPE = "rpi_matter_controller"
  _OWNER_EMAIL = "gdm-authors@google.com"

  @decorators.LogDecorator(logger)
  def factory_reset(self) -> None:
    """Factory resets the device."""
    self.matter_controller.factory_reset()

  @decorators.CapabilityDecorator(
      matter_controller_chip_tool.MatterControllerChipTool)
  def matter_controller(
      self) -> matter_controller_chip_tool.MatterControllerChipTool:
    """Matter controller capability to send chip-tool commands to the device."""
    return self.lazy_init(
        matter_controller_chip_tool.MatterControllerChipTool,
        device_name=self.name,
        regex_shell_fn=self.shell_with_regex,
        shell_fn=self.shell,
        send_file_to_device=self.file_transfer.send_file_to_device,
        get_property_fn=self.get_property,
        set_property_fn=self.set_property)

  @decorators.OptionalProperty
  def matter_node_id(self) -> Optional[int]:
    """Matter Node ID assigned to the currently commissioned end device."""
    return self.props["optional"].get("matter_node_id")

  @decorators.CapabilityDecorator(
      matter_endpoints_accessor_chip_tool.MatterEndpointsAccessorChipTool)
  def matter_endpoints(
      self
  ) -> matter_endpoints_accessor_chip_tool.MatterEndpointsAccessorChipTool:
    """Matter capability to access commissioned device's endpoint instances."""
    if self.matter_node_id is None:
      raise errors.DeviceError(
          "matter_endpoints requires a commissioned end device.")

    return self.lazy_init(
        matter_endpoints_accessor_chip_tool.MatterEndpointsAccessorChipTool,
        device_name=self.name,
        node_id_getter=lambda: self.matter_node_id,
        shell_fn=self.shell,
        shell_with_regex=self.shell_with_regex,
        matter_controller=self.matter_controller)
