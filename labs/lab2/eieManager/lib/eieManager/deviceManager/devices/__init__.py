from typing import Optional, List

"""
device module entry point.
"""
from ..device import Device

from .temp import TempDevice
from .level import LevelDevice
from .actuador import ActuadorDevice
from .sensor import SensorDevice

"""
Type of devices:


    -Sensor {READ, ON, OFF}
    -Actuador {ACTIVATE, ON, OFF}

"""


class DeviceFactory():
    """
    Factory that creates a device of a given type name.
    """
    def __init__(self) -> None:
        # Dictionary that maps names of sensor types to classes.
        self._device_type_to_cls = {
            "Temperature": TempDevice,
            "Level": LevelDevice,
            "Actuador": ActuadorDevice,
            "Sensor": SensorDevice
        }

    @property
    def supported_types(self):
        """
        Returns the list of names for the supported devices types.
        """
        return [dType for dType in self.device_type_to_cls.keys()]

    def __call__(self, name: str, dType: str, commands: List, ip: str)-> Device:
        """
        Creates the Device.

        :param str name: Name of the device to create.
        :param str dType: Device type.
        :param str commands: Device list of commands.
        :param str ip: Device ip reference.

        """
        
        device_cls = self._device_type_to_cls[dType]

        return device_cls(name)
