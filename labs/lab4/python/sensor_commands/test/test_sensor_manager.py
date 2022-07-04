from sensor_commands.sensor import sensor
from pytest import fixture
import logging
from sensor_commands.sensor.manager import SensorManager


@fixture
def sensor_mgr():
    config_name = "/home/dev/ws/labs/lab4/python/sensor_commands/config/sensors_cfg.json"
    sensor_man = SensorManager(config_name)
    logging.info("\nCreated Sensor Manager")
    return sensor_man


class MockSensor(sensor.Sensor):  # no tengo que instanciarla
    def __init__(self, name: str) -> None:
        super().__init__(name, "mock", "porUnidad")
        self._read_counter = 0

    def assert_read(self) -> bool:
        if (self._read_counter):
            return_val = 1
        else:
            return_val = 0
        return return_val

    def read(self) -> float:
        self._read_counter = 1
        print("Sensor was read in read function")
        return 0.1234  # random value


def test_sensor_manager_supported_types():
    pass


def test_sensor_manager_single_sensor_create_destroy():
    pass


def test_sensor_manager_single_sensor_read_command():
    pass


def test_sensor_manager_mock_type_register_unregister(sensor_mgr):
    mock = MockSensor("mockSensor")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    sensor_mgr.unregister_sensor_type(mock.type())


def test_sensor_manager_mock_sensor_create_destroy(sensor_mgr):
    mock = MockSensor("mockSensor")  # only 1 argument to be called later
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    sensor_mgr.create_sensor(mock.name(), 'mock')
    logging.info("\nGetting sensor info:")
    sensors_info = sensor_mgr.get_sensors_info()
    logging.info(f"\n{sensors_info}")
    sensor_mgr.destroy_sensor(mock.name())
    sensor_mgr.unregister_sensor_type(mock.type())


def test_sensor_manager_mock_sensor_read_command(sensor_mgr):
    mock = MockSensor("mockSensor")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    sensor_mgr.create_sensor(mock.name(), mock.type())
    sensor_mgr.get_sensors_info()
    sensor_read = sensor_mgr.create_sensor_read_cmd(mock.name())
    sensor_read.execute()
    sensor_was_read = mock.assert_read()
    print(sensor_was_read)
    print(f"mock.read_counter: {mock._read_counter}")
    sensor_mgr.destroy_sensor(mock.name())
    sensor_mgr.unregister_sensor_type(mock.type())
