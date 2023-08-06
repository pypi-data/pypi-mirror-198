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
"""Device controllers and capabilities built into GDM."""
from typing import Any, Dict

from gazoo_device import _version
from gazoo_device import config
from gazoo_device import data_types
from gazoo_device import detect_criteria
from gazoo_device import gdm_logger
from gazoo_device.auxiliary_devices import cambrionix
from gazoo_device.auxiliary_devices import dc2200
from gazoo_device.auxiliary_devices import dli_powerswitch
from gazoo_device.auxiliary_devices import dlink_switch
from gazoo_device.auxiliary_devices import efr32
from gazoo_device.auxiliary_devices import esp32
from gazoo_device.auxiliary_devices import m5stick
from gazoo_device.auxiliary_devices import nrf52840
from gazoo_device.auxiliary_devices import nrf_openthread
from gazoo_device.auxiliary_devices import raspberry_pi
from gazoo_device.auxiliary_devices import raspberry_pi_matter_controller
from gazoo_device.auxiliary_devices import unifi_poe_switch
from gazoo_device.auxiliary_devices import yepkit
from gazoo_device.capabilities import bluetooth_service_linux
from gazoo_device.capabilities import comm_power_default
from gazoo_device.capabilities import device_power_default
from gazoo_device.capabilities import embedded_script_dli_powerswitch
from gazoo_device.capabilities import event_parser_default
from gazoo_device.capabilities import fastboot_default
from gazoo_device.capabilities import file_transfer_adb
from gazoo_device.capabilities import file_transfer_docker
from gazoo_device.capabilities import file_transfer_echo
from gazoo_device.capabilities import file_transfer_scp
from gazoo_device.capabilities import flash_build_esptool
from gazoo_device.capabilities import flash_build_jlink
from gazoo_device.capabilities import flash_build_nrfjprog
from gazoo_device.capabilities import led_driver_default
from gazoo_device.capabilities import matter_controller_chip_tool
from gazoo_device.capabilities import matter_endpoints_accessor_chip_tool
from gazoo_device.capabilities import matter_endpoints_accessor_pw_rpc
from gazoo_device.capabilities import matter_sample_app_shell
from gazoo_device.capabilities import package_management_android
from gazoo_device.capabilities import pwrpc_button_default
from gazoo_device.capabilities import pwrpc_common_default
from gazoo_device.capabilities import pwrpc_wifi_default
from gazoo_device.capabilities import shell_ssh
from gazoo_device.capabilities import switch_power_dli_powerswitch
from gazoo_device.capabilities import switch_power_ethernet
from gazoo_device.capabilities import switch_power_snmp
from gazoo_device.capabilities import switch_power_unifi_switch
from gazoo_device.capabilities import switch_power_usb_default
from gazoo_device.capabilities import switch_power_usb_with_charge
from gazoo_device.capabilities import usb_hub_default
from gazoo_device.capabilities import wpan_nrf_ot
from gazoo_device.capabilities.interfaces import bluetooth_service_base
from gazoo_device.capabilities.interfaces import comm_power_base
from gazoo_device.capabilities.interfaces import device_power_base
from gazoo_device.capabilities.interfaces import embedded_script_base
from gazoo_device.capabilities.interfaces import event_parser_base
from gazoo_device.capabilities.interfaces import fastboot_base
from gazoo_device.capabilities.interfaces import file_transfer_base
from gazoo_device.capabilities.interfaces import flash_build_base
from gazoo_device.capabilities.interfaces import led_driver_base
from gazoo_device.capabilities.interfaces import matter_controller_base
from gazoo_device.capabilities.interfaces import matter_endpoints_base
from gazoo_device.capabilities.interfaces import matter_sample_app_base
from gazoo_device.capabilities.interfaces import package_management_base
from gazoo_device.capabilities.interfaces import pwrpc_button_base
from gazoo_device.capabilities.interfaces import pwrpc_common_base
from gazoo_device.capabilities.interfaces import pwrpc_wifi_base
from gazoo_device.capabilities.interfaces import shell_base
from gazoo_device.capabilities.interfaces import switch_power_base
from gazoo_device.capabilities.interfaces import switchboard_base
from gazoo_device.capabilities.interfaces import usb_hub_base
from gazoo_device.capabilities.interfaces import wpan_base
from gazoo_device.capabilities.matter_clusters import basic_information_chip_tool
from gazoo_device.capabilities.matter_clusters import boolean_state_pw_rpc
from gazoo_device.capabilities.matter_clusters import color_control_pw_rpc
from gazoo_device.capabilities.matter_clusters import door_lock_chip_tool
from gazoo_device.capabilities.matter_clusters import door_lock_pw_rpc
from gazoo_device.capabilities.matter_clusters import fan_control_pw_rpc
from gazoo_device.capabilities.matter_clusters import flow_measurement_chip_tool
from gazoo_device.capabilities.matter_clusters import flow_measurement_pw_rpc
from gazoo_device.capabilities.matter_clusters import illuminance_measurement_chip_tool
from gazoo_device.capabilities.matter_clusters import illuminance_measurement_pw_rpc
from gazoo_device.capabilities.matter_clusters import level_control_chip_tool
from gazoo_device.capabilities.matter_clusters import level_control_pw_rpc
from gazoo_device.capabilities.matter_clusters import occupancy_sensing_chip_tool
from gazoo_device.capabilities.matter_clusters import occupancy_sensing_pw_rpc
from gazoo_device.capabilities.matter_clusters import on_off_chip_tool
from gazoo_device.capabilities.matter_clusters import on_off_pw_rpc
from gazoo_device.capabilities.matter_clusters import pressure_measurement_chip_tool
from gazoo_device.capabilities.matter_clusters import pressure_measurement_pw_rpc
from gazoo_device.capabilities.matter_clusters import relative_humidity_measurement_chip_tool
from gazoo_device.capabilities.matter_clusters import relative_humidity_measurement_pw_rpc
from gazoo_device.capabilities.matter_clusters import temperature_measurement_chip_tool
from gazoo_device.capabilities.matter_clusters import temperature_measurement_pw_rpc
from gazoo_device.capabilities.matter_clusters import thermostat_chip_tool
from gazoo_device.capabilities.matter_clusters import thermostat_pw_rpc
from gazoo_device.capabilities.matter_clusters import window_covering_pw_rpc
from gazoo_device.capabilities.matter_clusters.interfaces import basic_information_base
from gazoo_device.capabilities.matter_clusters.interfaces import boolean_state_base
from gazoo_device.capabilities.matter_clusters.interfaces import color_control_base
from gazoo_device.capabilities.matter_clusters.interfaces import door_lock_base
from gazoo_device.capabilities.matter_clusters.interfaces import fan_control_base
from gazoo_device.capabilities.matter_clusters.interfaces import level_control_base
from gazoo_device.capabilities.matter_clusters.interfaces import measurement_base
from gazoo_device.capabilities.matter_clusters.interfaces import occupancy_sensing_base
from gazoo_device.capabilities.matter_clusters.interfaces import on_off_base
from gazoo_device.capabilities.matter_clusters.interfaces import thermostat_base
from gazoo_device.capabilities.matter_clusters.interfaces import window_covering_base
from gazoo_device.capabilities.matter_endpoints import color_temperature_light
from gazoo_device.capabilities.matter_endpoints import contact_sensor
from gazoo_device.capabilities.matter_endpoints import dimmable_light
from gazoo_device.capabilities.matter_endpoints import door_lock
from gazoo_device.capabilities.matter_endpoints import extended_color_light
from gazoo_device.capabilities.matter_endpoints import fan
from gazoo_device.capabilities.matter_endpoints import flow_sensor
from gazoo_device.capabilities.matter_endpoints import heating_cooling_unit
from gazoo_device.capabilities.matter_endpoints import humidity_sensor
from gazoo_device.capabilities.matter_endpoints import light_sensor
from gazoo_device.capabilities.matter_endpoints import occupancy_sensor
from gazoo_device.capabilities.matter_endpoints import on_off_light
from gazoo_device.capabilities.matter_endpoints import on_off_light_switch
from gazoo_device.capabilities.matter_endpoints import on_off_plugin_unit
from gazoo_device.capabilities.matter_endpoints import pressure_sensor
from gazoo_device.capabilities.matter_endpoints import root_node
from gazoo_device.capabilities.matter_endpoints import speaker
from gazoo_device.capabilities.matter_endpoints import temperature_sensor
from gazoo_device.capabilities.matter_endpoints import thermostat
from gazoo_device.capabilities.matter_endpoints import unsupported_endpoint
from gazoo_device.capabilities.matter_endpoints import window_covering
from gazoo_device.capabilities.matter_endpoints.interfaces import color_temperature_light_base
from gazoo_device.capabilities.matter_endpoints.interfaces import contact_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import dimmable_light_base
from gazoo_device.capabilities.matter_endpoints.interfaces import door_lock_base as door_lock_endpoint_base
from gazoo_device.capabilities.matter_endpoints.interfaces import extended_color_light_base
from gazoo_device.capabilities.matter_endpoints.interfaces import fan_base
from gazoo_device.capabilities.matter_endpoints.interfaces import flow_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import heating_cooling_unit_base
from gazoo_device.capabilities.matter_endpoints.interfaces import humidity_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import light_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import occupancy_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import on_off_light_base
from gazoo_device.capabilities.matter_endpoints.interfaces import on_off_light_switch_base
from gazoo_device.capabilities.matter_endpoints.interfaces import on_off_plugin_unit_base
from gazoo_device.capabilities.matter_endpoints.interfaces import pressure_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import root_node_base
from gazoo_device.capabilities.matter_endpoints.interfaces import speaker_base
from gazoo_device.capabilities.matter_endpoints.interfaces import temperature_sensor_base
from gazoo_device.capabilities.matter_endpoints.interfaces import thermostat_base as thermostat_endpoint_base
from gazoo_device.capabilities.matter_endpoints.interfaces import unsupported_endpoint_base
from gazoo_device.capabilities.matter_endpoints.interfaces import window_covering_base as window_covering_endpoint_base
from gazoo_device.primary_devices import efr32_matter
from gazoo_device.primary_devices import esp32_matter
from gazoo_device.primary_devices import nrf_matter
from gazoo_device.primary_devices import raspberry_pi_matter
from gazoo_device.switchboard import communication_types
from gazoo_device.switchboard import switchboard


__version__ = _version.version
_PUBLIC_KEY_SUFFIX = ".pub"
logger = gdm_logger.get_logger()


def download_key(key_info: data_types.KeyInfo, local_key_path: str) -> None:
  """Raises an error with instructions on how to generate or obtain a key.

  Args:
    key_info: Information about key to download.
    local_key_path: File to which the key should be stored.

  Raises:
    RuntimeError: Key has to be retrieved or generated manually.
  """
  base_error = f"GDM doesn't come with built-in SSH key {key_info}. "

  if local_key_path.endswith(_PUBLIC_KEY_SUFFIX):
    private_key_path = local_key_path[:-len(_PUBLIC_KEY_SUFFIX)]
  else:
    private_key_path = local_key_path
  how_to_fix = (
      "Run 'ssh-keygen' to generate your own key. "
      f"Select {private_key_path} as the file to which the key should be "
      "saved. Leave the passphrase empty.")
  raise RuntimeError(base_error + how_to_fix)


def export_extensions() -> Dict[str, Any]:
  """Exports built-in device controllers, capabilities, communication types."""
  return {
      "primary_devices": [
          esp32_matter.Esp32Matter,
          efr32_matter.Efr32Matter,
          nrf_matter.NrfMatter,
          raspberry_pi_matter.RaspberryPiMatter,
      ],
      "auxiliary_devices": [
          dc2200.DC2200,
          cambrionix.Cambrionix,
          dli_powerswitch.DliPowerSwitch,
          dlink_switch.DLinkSwitch,
          efr32.EFR32,
          esp32.ESP32,
          m5stick.M5Stick,
          nrf52840.NRF52840,
          nrf_openthread.NrfOpenThread,
          raspberry_pi.RaspberryPi,
          raspberry_pi_matter_controller.RaspberryPiMatterController,
          unifi_poe_switch.UnifiPoeSwitch,
          yepkit.Yepkit,
      ],
      "virtual_devices": [],
      "communication_types": [
          communication_types.AdbComms,
          communication_types.DockerComms,
          communication_types.JlinkSerialComms,
          communication_types.PigweedSerialComms,
          communication_types.PigweedSocketComms,
          communication_types.PtyProcessComms,
          communication_types.SerialComms,
          communication_types.SnmpComms,
          communication_types.SshComms,
          communication_types.UsbComms,
          communication_types.YepkitComms,
      ],
      "detect_criteria": detect_criteria.DETECT_CRITERIA,
      "capability_interfaces": [
          basic_information_base.BasicInformationClusterBase,
          bluetooth_service_base.BluetoothServiceBase,
          boolean_state_base.BooleanStateClusterBase,
          color_control_base.ColorControlClusterBase,
          color_temperature_light_base.ColorTemperatureLightBase,
          contact_sensor_base.ContactSensorBase,
          comm_power_base.CommPowerBase,
          device_power_base.DevicePowerBase,
          dimmable_light_base.DimmableLightBase,
          door_lock_endpoint_base.DoorLockBase,
          door_lock_base.DoorLockClusterBase,
          extended_color_light_base.ExtendedColorLightBase,
          embedded_script_base.EmbeddedScriptBase,
          event_parser_base.EventParserBase,
          fan_base.FanBase,
          fan_control_base.FanControlClusterBase,
          fastboot_base.FastbootBase,
          file_transfer_base.FileTransferBase,
          flash_build_base.FlashBuildBase,
          flow_sensor_base.FlowSensorBase,
          heating_cooling_unit_base.HeatingCoolingUnitBase,
          humidity_sensor_base.HumiditySensorBase,
          led_driver_base.LedDriverBase,
          level_control_base.LevelControlClusterBase,
          light_sensor_base.LightSensorBase,
          matter_controller_base.MatterControllerBase,
          matter_endpoints_base.MatterEndpointsBase,
          matter_sample_app_base.MatterSampleAppBase,
          measurement_base.MeasurementClusterBase,
          occupancy_sensing_base.OccupancySensingClusterBase,
          occupancy_sensor_base.OccupancySensorBase,
          on_off_base.OnOffClusterBase,
          on_off_light_base.OnOffLightBase,
          on_off_light_switch_base.OnOffLightSwitchBase,
          on_off_plugin_unit_base.OnOffPluginUnitBase,
          package_management_base.PackageManagementBase,
          pressure_sensor_base.PressureSensorBase,
          pwrpc_button_base.PwRPCButtonBase,
          pwrpc_common_base.PwRPCCommonBase,
          pwrpc_wifi_base.PwRPCWifiBase,
          root_node_base.RootNodeBase,
          shell_base.ShellBase,
          speaker_base.SpeakerBase,
          switchboard_base.SwitchboardBase,
          switch_power_base.SwitchPowerBase,
          temperature_sensor_base.TemperatureSensorBase,
          thermostat_base.ThermostatClusterBase,
          thermostat_endpoint_base.ThermostatBase,
          unsupported_endpoint_base.UnsupportedBase,
          usb_hub_base.UsbHubBase,
          window_covering_base.WindowCoveringClusterBase,
          window_covering_endpoint_base.WindowCoveringBase,
          wpan_base.WpanBase,
      ],
      "capability_flavors": [
          basic_information_chip_tool.BasicInformationClusterChipTool,
          bluetooth_service_linux.BluetoothServiceLinux,
          boolean_state_pw_rpc.BooleanStateClusterPwRpc,
          color_control_pw_rpc.ColorControlClusterPwRpc,
          color_temperature_light.ColorTemperatureLightEndpoint,
          contact_sensor.ContactSensorEndpoint,
          comm_power_default.CommPowerDefault,
          device_power_default.DevicePowerDefault,
          dimmable_light.DimmableLightEndpoint,
          door_lock.DoorLockEndpoint,
          door_lock_chip_tool.DoorLockClusterChipTool,
          door_lock_pw_rpc.DoorLockClusterPwRpc,
          embedded_script_dli_powerswitch.EmbeddedScriptDliPowerswitch,
          event_parser_default.EventParserDefault,
          extended_color_light.ExtendedColorLightEndpoint,
          fan.FanEndpoint,
          fan_control_pw_rpc.FanControlClusterPwRpc,
          fastboot_default.FastbootDefault,
          file_transfer_adb.FileTransferAdb,
          file_transfer_docker.FileTransferDocker,
          file_transfer_echo.FileTransferEcho,
          file_transfer_scp.FileTransferScp,
          flash_build_esptool.FlashBuildEsptool,
          flash_build_jlink.FlashBuildJLink,
          flash_build_nrfjprog.FlashBuildNrfjprog,
          flow_measurement_chip_tool.FlowMeasurementClusterChipTool,
          flow_measurement_pw_rpc.FlowMeasurementClusterPwRpc,
          flow_sensor.FlowSensorEndpoint,
          heating_cooling_unit.HeatingCoolingUnitEndpoint,
          humidity_sensor.HumiditySensorEndpoint,
          illuminance_measurement_chip_tool.
          IlluminanceMeasurementClusterChipTool,
          illuminance_measurement_pw_rpc.IlluminanceMeasurementClusterPwRpc,
          led_driver_default.LedDriverDefault,
          level_control_chip_tool.LevelControlClusterChipTool,
          level_control_pw_rpc.LevelControlClusterPwRpc,
          light_sensor.LightSensorEndpoint,
          matter_controller_chip_tool.MatterControllerChipTool,
          matter_endpoints_accessor_chip_tool.MatterEndpointsAccessorChipTool,
          matter_endpoints_accessor_pw_rpc.MatterEndpointsAccessorPwRpc,
          matter_sample_app_shell.MatterSampleAppShell,
          occupancy_sensing_chip_tool.OccupancySensingClusterChipTool,
          occupancy_sensing_pw_rpc.OccupancySensingClusterPwRpc,
          occupancy_sensor.OccupancySensorEndpoint,
          on_off_light.OnOffLightEndpoint,
          on_off_light_switch.OnOffLightSwitchEndpoint,
          on_off_chip_tool.OnOffClusterChipTool,
          on_off_plugin_unit.OnOffPluginUnitEndpoint,
          on_off_pw_rpc.OnOffClusterPwRpc,
          temperature_measurement_pw_rpc.TemperatureMeasurementClusterPwRpc,
          package_management_android.PackageManagementAndroid,
          pressure_sensor.PressureSensorEndpoint,
          pressure_measurement_chip_tool.PressureMeasurementClusterChipTool,
          pressure_measurement_pw_rpc.PressureMeasurementClusterPwRpc,
          pwrpc_button_default.PwRPCButtonDefault,
          pwrpc_common_default.PwRPCCommonDefault,
          pwrpc_wifi_default.PwRPCWifiDefault,
          (relative_humidity_measurement_chip_tool.
           RelativeHumidityMeasurementClusterChipTool),
          (relative_humidity_measurement_pw_rpc.
           RelativeHumidityMeasurementClusterPwRpc),
          root_node.RootNodeEndpoint,
          shell_ssh.ShellSSH,
          speaker.SpeakerEndpoint,
          switch_power_dli_powerswitch.SwitchPowerDliPowerswitch,
          switch_power_ethernet.SwitchPowerEthernet,
          switch_power_snmp.SwitchPowerSnmp,
          switch_power_unifi_switch.SwitchPowerUnifiSwitch,
          switch_power_usb_default.SwitchPowerUsbDefault,
          switch_power_usb_with_charge.SwitchPowerUsbWithCharge,
          switchboard.SwitchboardDefault,
          temperature_sensor.TemperatureSensorEndpoint,
          temperature_measurement_chip_tool.
          TemperatureMeasurementClusterChipTool,
          temperature_measurement_pw_rpc.TemperatureMeasurementClusterPwRpc,
          thermostat.ThermostatEndpoint,
          thermostat_chip_tool.ThermostatClusterChipTool,
          thermostat_pw_rpc.ThermostatClusterPwRpc,
          unsupported_endpoint.UnsupportedEndpoint,
          usb_hub_default.UsbHubDefault,
          window_covering.WindowCoveringEndpoint,
          window_covering_pw_rpc.WindowCoveringClusterPwRpc,
          wpan_nrf_ot.WpanNrfOt,
      ],
      "keys": list(config.KEYS.values()),
  }
