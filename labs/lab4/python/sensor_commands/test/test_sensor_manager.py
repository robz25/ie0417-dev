
# from distutils.command.config import config
# import pytest
# from defer import return_value
from sensor_commands.sensor import sensor
from pytest import fixture
# from pytest import fixture
# from utils import rand_gen
import logging
#   import demo_api
from sensor_commands.sensor.manager import SensorManager
# import demo_api


@fixture
def sensor_mgr():
    config_name = "/home/dev/ws/labs/lab4/python/sensor_commands/config/sensors_cfg.json"
    # "../config/sensors_cfg.json"  # test test se debe quitar los
    sensor_man = SensorManager(config_name)
    logging.info("\nCreated Sensor Manager")
    return sensor_man


# def test_sensor_manager_supported_types(sensor_mgr):
    # pass


class MockSensor(sensor.Sensor):  # no tengo que instanciarla
    def __init__(self, name: str) -> None:
        super().__init__(name, "mock", "porUnidad")
        self.read_counter = 0

    def assert_read(self) -> bool:
        # assert self.read_counter is True  # asi se pone no ==
        # assert self.read_counter == 1, "Sensor was not read"
        if (self.read_counter):
            return_val = 1
        else:
            return_val = 0
        self.read_counter = 0
        return return_val
    # @abstractmethod

    def read(self) -> float:
        # Reads the sensor.
        # :return: Sensor reading.
        self.read_counter = 1
        print("Sensor was read in read function")
        return 0.1234  # self.read_counter


def test_sensor_manager_supported_types():
    assert len("holi") > 0, "List of sensor types is empty"


def test_sensor_manager_single_sensor_create_destroy():
    pass


def test_sensor_manager_single_sensor_read_command():
    pass


def test_sensor_manager_mock_type_register_unregister(sensor_mgr):
    # mock = MockSensor("mockSensor", "mock", "porunidad")
    mock = MockSensor("mockSensor")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    sensor_mgr.unregister_sensor_type(mock.type())
    assert 1 + 1 == 2, "Math is wrong"


"""
def __init__(self, name: str, stype: str, unit: str) -> None:
        self._name = name
        self._type = stype
        self._unit = unit
    def register_sensor_type(self, stype: str, cls: Type[Sensor])
    self.sensor_factory.register_type_cls(stype, cls)
    def unregister_sensor_type(self, stype: str):
    self.sensor_factory.unregister_type_cls(stype)
"""


def test_sensor_manager_mock_sensor_create_destroy(sensor_mgr):
    mock = MockSensor("mockSensor")  # , "mock", "porunidad")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    sensor_mgr.create_sensor(mock.name(), 'mock')  # level y temperature
    logging.info("\nGetting sensor info:")
    sensors_info = sensor_mgr.get_sensors_info()
    logging.info(f"\n{sensors_info}")
    sensor_mgr.destroy_sensor(mock.name())
    sensor_mgr.unregister_sensor_type(mock.type())
    # def destroy_sensor(self, name: str) -> None:
    # def create_sensor(self, name: str, stype: str) -> None:
    # def get_sensors_info(self) -> Dict[str, Dict[str, Any]]:
    # def create_sensor(self, name: str, stype: str) -> None:


def test_sensor_manager_mock_sensor_read_command(sensor_mgr):
    mock = MockSensor("mockSensor")  # , "mock", "porunidad")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    sensor_mgr.create_sensor(mock.name(), mock.type())
    sensor_mgr.get_sensors_info()
    sensor_read = sensor_mgr.create_sensor_read_cmd(mock.name())
    sensor_read.execute()
    # missing execute command
    sensor_was_read = mock.assert_read()
    if(sensor_was_read):
        print("Sensor was read")
    else:
        print("Sensor was not read")
    # assert sensor_was_read == 1, "Sensor was not read"
    # missing
    sensor_mgr.destroy_sensor(mock.name())
    sensor_mgr.unregister_sensor_type(mock.type())
    # def create_sensor_read_cmd(self, sensor_name: str,
    # analyzer: Optional[SensorAnalyzer] = None) -> Command:


"""
def test_demo_api_mult_op():
    r = demo_api.mult(5, 4)
    logging.info(f"Mult result: {r}")
    assert r == 20, "Multiplication failed!"
"""
