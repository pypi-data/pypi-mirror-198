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

"""Interface for a Matter Extended color light endpoint."""
import abc
from gazoo_device.capabilities.matter_clusters.interfaces import color_control_base
from gazoo_device.capabilities.matter_clusters.interfaces import level_control_base
from gazoo_device.capabilities.matter_clusters.interfaces import on_off_base
from gazoo_device.capabilities.matter_endpoints.interfaces import endpoint_base


class ExtendedColorLightBase(
    endpoint_base.EndpointBase, metaclass=abc.ABCMeta):
  """Matter Extended color light endpoint interface."""

  DEVICE_TYPE_ID = 0x010D

  @property
  @abc.abstractmethod
  def on_off(self) -> on_off_base.OnOffClusterBase:
    """Required cluster: ZCL on_off cluster."""

  @property
  @abc.abstractmethod
  def level_control(self) -> level_control_base.LevelControlClusterBase:
    """Required cluster: ZCL level cluster."""

  @property
  @abc.abstractmethod
  def color_control(self) -> color_control_base.ColorControlClusterBase:
    """Required cluster: ZCL color control cluster."""

  # TODO(b/209362086) Add the below clusters
  # @abc.abstractproperty
  # def scenes(self):
  #   """Required cluster: ZCL scenes cluster."""

  # @abc.abstractproperty
  # def groups(self):
  #   """Required cluster: ZCL groups cluster."""
