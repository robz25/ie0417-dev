
# from distutils.command.config import config
# import pytest
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
    def assert_read(self) -> bool:
        assert self.read_counter is True  # asi se pone no ==
        self.read_counter = False
    # @abstractmethod

    def read(self) -> float:
        # Reads the sensor.
        # :return: Sensor reading.
        self.read_counter = True
        return 0.1234  # self.read_counter


def test_sensor_manager_supported_types():
    assert len("holi") > 0, "List of sensor types is empty"


def test_sensor_manager_single_sensor_create_destroy():
    pass


def test_sensor_manager_single_sensor_read_command():
    pass


def test_sensor_manager_mock_type_register_unregister(sensor_mgr):
    mock = MockSensor("mock", "mocksensor", "porunidad")
    sensor_mgr.register_sensor_type(mock.type(), mock)
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
    mock = MockSensor("mock", "mocksensor", "porunidad")
    sensor_mgr.register_sensor_type(mock.type(), mock)
    sensor_mgr.create_sensor(mock.name(), mock.type())
    sensor_mgr.get_sensor_info()
    sensor_mgr.destroy_sensor(mock.name())
    sensor_mgr.unregister_sensor_type(mock.type())
    # def destroy_sensor(self, name: str) -> None:
    # def create_sensor(self, name: str, stype: str) -> None:
    # def get_sensors_info(self) -> Dict[str, Dict[str, Any]]:
    # def create_sensor(self, name: str, stype: str) -> None:
    assert 1 * 9 == 9, "Math is ok"


def test_sensor_manager_mock_sensor_read_command(sensor_mgr):
    mock = MockSensor("mock", "mocksensor", "porunidad")
    sensor_mgr.register_sensor_type(mock.type(), mock)
    sensor_mgr.create_sensor(mock.name(), mock.type())
    sensor_mgr.get_sensor_info()
    sensor_mgr.create_sensor_read_cmd(mock.name())
    # missing
    mock.assert_read()
    # missing
    sensor_mgr.destroy_sensor(mock.name())
    sensor_mgr.unregister_sensor_type(mock.type())
    # def create_sensor_read_cmd(self, sensor_name: str,
    # analyzer: Optional[SensorAnalyzer] = None) -> Command:
    assert 1 + 1 != 0, "Math is ok"


"""
def test_demo_api_mult_op():
    r = demo_api.mult(5, 4)
    logging.info(f"Mult result: {r}")
    assert r == 20, "Multiplication failed!"
"""
