import json
from typing import Optional, List, Dict

from ..command import Command
from .devices import DeviceFactory
from .device import Device, DeviceReadCommand, DeviceAnalyzer


class DeviceManager:
    """
    Manager class to control device objects lifecycle.

    :param str config_filename: Name of the file with the devices config.
    """
    def __init__(self, config_filename: str) -> None:
        self.config_filename = config_filename
        self.device_factory = DeviceFactory()
        self.devices: Dict[str, Device] = {}
        self.devices_per_type: Dict[str, Dict[str, Device]] = {}
        self.init_config()

    def _init_devices_per_type(self):
        """
        Initializes a devices per-type mapping dictionary.
        """
        for device in self.devices.values():
            dType = device.dType()
            name = device.name()
            commands = device.commands()
            ip = device.ip()

            if dType not in self.devices_per_type:
                self.devices_per_type[dType] = {}
            #------------------ 
            self.devices_per_type[dType][name] = device

    def init_config(self) -> None:
        """
        Initializes the manager configuration.
        """
        # Parse config file
        with open(self.config_filename) as config_file:
            config_info = json.load(config_file)
            devices_info = config_info["Devices"]
            # Create devices
            for device_info in devices_info:
                name = device_info["name"]
                dType = device_info["type"]
                commands = device_info["commands"]
                ip = device_info["ip"]
                #Add more types

                #Call deviceFactory
                self.devices[name] = self.device_factory(name, dType, commands, ip)

        self._init_devices_per_type()

    def get_device_types(self) -> List[str]:
        """
        Returns the list of device types.
        """
        return [name for name in self.devices_per_type.keys()]

    def get_device_names(self) -> List[str]:
        """
        Returns the list of device names.
        """
        return [name for name in self.devices.keys()]

    def get_device_names_per_type(self, stype: str) -> List[str]:
        """
        Returns the list of device names for a device type.
        """
        names: List[str] = []
        type_devices = self.devices_per_type.get(stype)
        if type_devices is not None:
            names = [name for name in type_devices.keys()]
        return names

    def create_device_read_cmd(
            self,
            device_name: str,
            analyzer: Optional[DeviceAnalyzer] = None
    ) -> Command:
        """
        Creates a command to read a device.

        :param str device_name: Name of the device to read.
        :param device_name: Name of the device to read.
        :param analyzer: device analyzer to send the readings.
        :type analyzer: :class:`DeviceAnalyzer`
        """
        device = self.devices[device_name]
        return DeviceReadCommand(device, analyzer)
