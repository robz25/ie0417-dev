from typing import Optional, List

from abc import ABC, abstractmethod

from ..command import Command


class Device(ABC):
    """
    Generic Device representation.

    :param str name: Name of the Device.
    :param str dType: Type of the Device.
    :param str commands: List of commands supported by the device.
    :param str ip: Connection info. Format -> host:port
    """
    def __init__(self, name: str, dType: str, commands: List, ip: str) -> None:
        self._name = name
        self._dType = type
        self._commands = commands
        self._ip = ip

    def name(self) -> str:
        """
        Gets the name of the Device.
        """
        return self._name

    def dType(self) -> str:
        """
        Gets the type of the Device.
        """
        return self._dType

    def commands(self) -> List:
        """
        Gets the list of commands for the Device.
        """
        return self._commands

    def ip(self) -> str:
        """
        Gets the ip of the Device.
        """
        return self._ip

    @abstractmethod
    def read(self) -> float:
        """
        Reads the Device.
        :return: Device reading.
        """
        pass


class DeviceAnalyzer(ABC):
    """
    Generic Device analyzer that processes updates from Device reads.
    """
    @abstractmethod
    def update(self, value: float):
        """
        Updates the analyzer state with a new Device reading.

        :param float value: Device reading value.
        """
        pass


class DeviceReadCommand(Command):
    """
    Command to read a Device and optionally update a DeviceAnalyzer.

    :param Device: Device object.
    :type Device: :class:`Device`
    :param analyzer: DeviceAnalyzer object or None.
    :type analyzer: :class:`DeviceAnalyzer` or None.
    """
    def __init__(
            self,
            Device: Device,
            analyzer: Optional[DeviceAnalyzer] = None
    ) -> None:
        self.Device = Device
        self.analyzer = analyzer

    def execute(self) -> None:
        """
        Reads the Device and optionally send value to analyzer.
        """
        name = self.Device.name()
        dType = self.Device.dType()
        commands = self.Device.commands()
        value = self.Device.read()

        if self.analyzer is not None:
            self.analyzer.update(value)
        print(f"DeviceReadCommand: [{dType}] {name}: {value} {ip}")
