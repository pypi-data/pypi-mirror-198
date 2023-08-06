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

"""Raspberry Pi device class."""
from gazoo_device import detect_criteria
from gazoo_device import gdm_logger
from gazoo_device.base_classes import raspbian_device

logger = gdm_logger.get_logger()


class RaspberryPi(raspbian_device.RaspbianDevice):
  """Base Class for RaspberryPi Devices.

  Supports the following functionality:
      --logging
      --shell
      --reboot
  """
  DETECT_MATCH_CRITERIA = {
      detect_criteria.SshQuery.IS_RASPBIAN_RPI: True,
      detect_criteria.SshQuery.IS_CHIP_TOOL_PRESENT: False,
      detect_criteria.SshQuery.IS_MATTER_LINUX_APP_RUNNING: False,
  }
  DEVICE_TYPE = "raspberrypi"
  _OWNER_EMAIL = "gdm-authors@google.com"
