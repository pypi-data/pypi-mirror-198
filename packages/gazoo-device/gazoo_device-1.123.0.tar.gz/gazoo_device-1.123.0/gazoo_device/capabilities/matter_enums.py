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

"""Matter spec enum module."""
import enum
from gazoo_device.protos import attributes_service_pb2

# The Matter cluster enums definitions: (only enums used in GDM are defined)


class ColorControlCluster(enum.IntEnum):
  """Color control cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_COLOR_CONTROL_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_CURRENT_HUE = 0x0000
  ATTRIBUTE_CURRENT_SATURATION = 0x0001
  ATTRIBUTE_COLOR_TEMPERATURE_MIREDS = 0x0007


class DoorLockCluster(enum.IntEnum):
  """Door lock cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_DOOR_LOCK_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_LOCK_STATE = 0x0000


class FlowMeasurementCluster(enum.IntEnum):
  """Flow Measurement cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_FLOW_MEASUREMENT_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_MEASURED_VALUE = 0x0000
  ATTRIBUTE_MIN_MEASURED_VALUE = 0x0001
  ATTRIBUTE_MAX_MEASURED_VALUE = 0x0002


class FanControlCluster(enum.IntEnum):
  """Fan Control cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_FAN_CONTROL_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_FAN_MODE = 0x0000
  ATTRIBUTE_FAN_MODE_SEQUENCE = 0x0001
  ATTRIBUTE_PERCENT_SETTING = 0x0002
  ATTRIBUTE_PERCENT_CURRENT = 0x0003
  ATTRIBUTE_SPEED_MAX = 0x0004
  ATTRIBUTE_SPEED_SETTING = 0x0005
  ATTRIBUTE_SPEED_CURRENT = 0x0006


class FanMode(enum.IntEnum):
  """Fan Mode attribute enum.
  """
  OFF = 0
  LOW = 1
  MEDIUM = 2
  HIGH = 3
  ON = 4
  AUTO = 5
  SMART = 6


class FanModeSequence(enum.IntEnum):
  """Fan Mode Sequence attribute enum.
  """
  OFF_LOW_MED_HIGH = 0
  OFF_LOW_HIGH = 1
  OFF_LOW_MED_HIGH_AUTO = 2
  OFF_LOW_HIGH_AUTO = 3
  OFF_ON_AUTO = 4
  OFF_ON = 5


class IlluminanceMeasurementCluster(enum.IntEnum):
  """Illuminance Measurement cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_ILLUMINANCE_MEASUREMENT_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_MEASURED_VALUE = 0x0000
  ATTRIBUTE_MIN_MEASURED_VALUE = 0x0001
  ATTRIBUTE_MAX_MEASURED_VALUE = 0x0002
  ATTRIBUTE_LIGHT_SENSOR_TYPE = 0x0004


class LightSensorType(enum.IntEnum):
  """LightSensorType attribute.
  """
  PHOTODIODE = 0
  CMOS = 1


class LevelControlCluster(enum.IntEnum):
  """Level control cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_LEVEL_CONTROL_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_CURRENT_LEVEL = 0x0000
  ATTRIBUTE_MIN_LEVEL = 0x0002
  ATTRIBUTE_MAX_LEVEL = 0x0003


class OccupancySensingCluster(enum.IntEnum):
  """Occupacny sensing cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_OCCUPANCY_SENSING_CLUSTER_ID

  # Attributes ID
  ATTRIBUTE_OCCUPANCY = 0x0000
  ATTRIBUTE_OCCUPANCY_SENSOR_TYPE = 0x0001
  ATTRIBUTE_OCCUPANCY_SENSOR_TYPE_BITMAP = 0x0002


class OnOffCluster(enum.IntEnum):
  """OnOff cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_ON_OFF_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_ON_OFF = 0x0000


class PressureMeasurementCluster(enum.IntEnum):
  """Pressure Measurement cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_PRESSURE_MEASUREMENT_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_MEASURED_VALUE = 0
  ATTRIBUTE_MIN_MEASURED_VALUE = 1
  ATTRIBUTE_MAX_MEASURED_VALUE = 2


class RelativeHumidityMeasurementCluster(enum.IntEnum):
  """Relative Humidity Measurement cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_RELATIVE_HUMIDITY_MEASUREMENT_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_MEASURED_VALUE = 0
  ATTRIBUTE_MIN_MEASURED_VALUE = 1
  ATTRIBUTE_MAX_MEASURED_VALUE = 2


class TemperatureMeasurementCluster(enum.IntEnum):
  """Temperature Measurement cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_TEMP_MEASUREMENT_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_MEASURED_VALUE = 0
  ATTRIBUTE_MIN_MEASURED_VALUE = 1
  ATTRIBUTE_MAX_MEASURED_VALUE = 2


# Lock state attribute enums
class LockState(enum.IntEnum):
  """Lock state attribute values.
  """
  NOT_FULLY_LOCKED = 0
  LOCKED = 1
  UNLOCKED = 2


# Occupancy Sensor type enums.
class OccupancySensorType(enum.IntEnum):
  """Occupancy Sensor type.
  """
  PIR = 0
  ULTRASONIC = 1
  PIR_AND_ULTRASONIC = 2
  PHYSICAL_CONTACT = 3


class BooleanStateCluster(enum.IntEnum):
  """Boolean State cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_BOOLEAN_STATE_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_STATE_VALUE = 0


class ThermostatCluster(enum.IntEnum):
  """Thermostat cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_THERMOSTAT_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_LOCAL_TEMPERATURE = 0x0000
  ATTRIBUTE_OCCUPIED_COOLING_SETPOINT = 0x0011
  ATTRIBUTE_OCCUPIED_HEATING_SETPOINT = 0x0012
  ATTRIBUTE_CONTROL_SEQUENCE_OF_OPERATION = 0x001b
  ATTRIBUTE_SYSTEM_MODE = 0x001c


class ThermostatControlSequence(enum.IntEnum):
  """Thermostat Control Sequence.

  The enum values are defined in the Matter spec.
  """

  COOLING_ONLY = 0
  COLLING_WITH_REHEAT = 1
  HEATING_ONLY = 2
  HEATING_WITH_REHEAT = 3
  COOLING_AND_HEATING = 4
  COOLING_AND_HEATING_WITH_REHEAT = 5


class ThermostatSystemMode(enum.IntEnum):
  """Thermostat System Mode.

  The enum values are defined in the Matter spec.
  """

  OFF = 0
  AUTO = 1
  COOL = 3
  HEAT = 4
  EMERGENCY_HEAT = 5
  PRECOOLING = 6
  FAN_ONLY = 7
  DRY = 8
  SLEEP = 9


class ThermostatSetpointMode(enum.IntEnum):
  """Thermostat Setpoint Mode.

  The enum values are defined in the Matter spec.
  """

  HEAT = 0
  COOL = 1
  BOTH = 2


class BasicInformationCluster(enum.IntEnum):
  """Basic information cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_BASIC_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_DATA_MODEL_REVISION = 0x0000
  ATTRIBUTE_VENDOR_NAME = 0x0001
  ATTRIBUTE_VENDOR_ID = 0x0002
  ATTRIBUTE_PRODUCT_NAME = 0x0003
  ATTRIBUTE_PRODUCT_ID = 0x0004
  ATTRIBUTE_NODE_LABEL = 0x0005
  ATTRIBUTE_LOCATION = 0x0006
  ATTRIBUTE_HARDWARE_VERSION = 0x0007
  ATTRIBUTE_HARDWARE_VERSION_STRING = 0x008
  ATTRIBUTE_SOFTWARE_VERSION = 0x009
  ATTRIBUTE_SOFTWARE_VERSION_STRING = 0x00A


class WindowCoveringCluster(enum.IntEnum):
  """Window Covering cluster ID and its attribute IDs.

  The enum values are defined in the Matter spec.
  """
  ID = attributes_service_pb2.ClusterType.ZCL_WINDOW_COVERING_CLUSTER_ID

  # Attribute IDs
  ATTRIBUTE_CURRENT_POSITION_LIFT_PERCENTAGE = 0x0008
  ATTRIBUTE_CURRENT_POSITION_TILT_PERCENTAGE = 0x0009

