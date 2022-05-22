from random import randint

from ..device import Device


class TempDevice(Device):
    def __init__(self, name: str) -> None:
        super().__init__(name, "temperature", "celsius")

    def read(self) -> float:
        return randint(0, 100)
