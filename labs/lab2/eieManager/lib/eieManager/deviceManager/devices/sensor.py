from random import randint

from ..device import Device


class SensorDevice(Device):
    def __init__(self, name: str) -> None:
        super().__init__(name, "sensor", ["A","B"],"1")

    def read(self) -> float:
        return randint(1, 128)
