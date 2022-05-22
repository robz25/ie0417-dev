from random import randint

from ..device import Device


class LuxDevice(Device):
    def __init__(self, name: str) -> None:
        super().__init__(name, "lux", "lux")

    def read(self) -> float:
        return randint(1, 128)
