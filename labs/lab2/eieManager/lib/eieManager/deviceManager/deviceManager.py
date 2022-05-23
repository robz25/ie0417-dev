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

    def create_device(self, name: str, type: str, commands: List, ip: str):
        """
        Creates a new device.

        :param str device_name: Name of the device to read.
        :param device_name: Name of the device to read.
        """
        json_data = {
        "name":name,
        "type":type,
        "commands":commands,
        "ip": ip
        }




        #with open(self.config_filename) as config_file:
        #    config_info = json.load(config_file)
        #    devices_info = config_info["Devices"]
        #    #devices_info.append(json_data)
        #    devices_info["namek"] = "jue"
        #data = json.load(jsonFile) # Read the JSON into the buffer
        #jsonFile = open(self.config_filename, "r") # Open the JSON file for reading
        #devices_info = data["Devices"]



        #jsonFile.close() # Close the JSON file
        #var = 2.4
        #data['name']=json_data
        #data[0] = var
        ## Save our changes to JSON file
        #jsonFile = open(self.config_filename, "w+")
        #jsonFile.write(json.dumps(data))
        #jsonFile.close()

        return 0

        #------------------------------------

    # function to add to JSON
    def write_json(self, name: str, type: str, commands: List, ip: str):

        json_data = {
        "name":name,
        "type":type,
        "commands":commands,
        "ip": ip
        }

        with open(self.config_filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["Devices"].append(json_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
 
        return 0

        #------------------------------------

    def delete_device(self, name: str):
        """Destroy a device with the name.

        :param str device_name: Name of the device to read.
        :param device_name: Name of the device to read.
        """
        with open(self.config_filename, 'w') as jsonFile:
            json.dump(json_data, jsonFile)
        jsonFile.close()

        for device in self.devices.values():
            dType = device.dType()
            name = device.name()
            commands = device.commands()
            ip = device.ip()

            if dType not in self.devices_per_type: 
                self.devices_per_type[dType] = {}
            #------------------ 
            self.devices_per_type[dType][name] = device

    def update_device():
        pass

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
            analyzer: Optional[DeviceAnalyzer] = None) -> Command:
        """
        Creates a command to read a device.

        :param str device_name: Name of the device to read.
        :param device_name: Name of the device to read.
        :param analyzer: device analyzer to send the readings.
        :type analyzer: :class:`DeviceAnalyzer`
        """
        device = self.devices[device_name]
        return DeviceReadCommand(device, analyzer)
