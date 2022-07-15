<<<<<<< HEAD

from distutils.command.config import config
import pytest

from sensor_commands.sensor.manager import SensorManager
import demo_api

@fixture
def sensor_mgr():
    config_name = "../config/sensors_cfg.json" # Definir path absoluto con respecto al contenedor
    return sensor_man

def test_sensor_manager_supported_types(sensor_mgr):

    pass



def test_sensor_manager_supported_types(sensor_mgr):

    pass

def test_demo_api_mult_op():
    r = demo_api.mult(5, 4)
    logging.info(f"Mult result: {r}")
    assert r == 20, "Multiplication failed!"
=======
from sensor_commands.sensor import sensor
from pytest import fixture
import pytest
from utils import rand_gen
import logging
from sensor_commands.sensor.manager import SensorManager
# if doesn't run rebuild: tox -re test


class FixtureContext:
    def __init__(self):
        self.rng = rand_gen.RandomGenerator()


@fixture
def rnd_gen():
    ctx = FixtureContext()
    yield ctx
    # NOTE: We return here after the test function finishes
    logging.info("Fixture teardown!")


@fixture
def sensor_mgr():
    config_name = "/home/dev/ws/labs/lab4/python/sensor_commands/config/sensors_cfg.json"
    sensor_man = SensorManager(config_name)
    logging.info("\nCreated Sensor Manager")
    return sensor_man


class MockSensor(sensor.Sensor):
    def __init__(self, name: str) -> None:
        super().__init__(name, "mock", "porUnidad")
        self._read_counter = 0

    def assert_read(self):
        assert self._read_counter == 0, "Sensor wasn't read"

    def read(self):
        self._read_counter = 1
        print("Sensor was read in read function")


def test_sensor_manager_supported_types(sensor_mgr):
    sensor_list = sensor_mgr.get_supported_sensor_types()
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    logging.info("\nGot supported types")
    assert len(sensor_list) > 0, "List of sensor types is empty"
    logging.info("\nFinished test")


def test_sensor_manager_single_sensor_create_destroy(sensor_mgr, rnd_gen):
    new_sen_name = "new_sensor"
    new_sen_type = sensor_mgr.get_supported_sensor_types()
    new_sen_type = new_sen_type[rnd_gen.rng.get_unique_int_list(low=0, high=1, num=1)[0]]
    sensor_mgr.create_sensor(new_sen_name, new_sen_type)
    logging.info(f"\nCreated mew sensor {new_sen_name} with type {new_sen_type}")
    with pytest.raises(Exception) as exception_info:
        sensor_mgr.create_sensor(new_sen_name, new_sen_type)
    assert str(exception_info.value) == 'Sensor with name new_sensor already exists'
    sensor_mgr.destroy_sensor(new_sen_name)
    logging.info("\nDestroyed sensor")
    sensors_info = sensor_mgr.get_sensors_info()
    with pytest.raises(KeyError) as exception_info:
        sensors_info[new_sen_name]
    assert str(exception_info.value) == '\'' + new_sen_name + '\''  # could also compare old value
    with pytest.raises(Exception) as exception_info:
        sensor_mgr.destroy_sensor(new_sen_name)
    assert str(exception_info.value) == "Sensor with name " + new_sen_name + " does not exist"
    logging.info("\nFinished test")


def test_sensor_manager_single_sensor_read_command(sensor_mgr, rnd_gen):
    new_sen_name = "new_sensor"
    new_sen_type = sensor_mgr.get_supported_sensor_types()
    new_sen_type = new_sen_type[rnd_gen.rng.get_unique_int_list(low=0, high=1, num=1)[0]]
    print(new_sen_type)
    sensor_mgr.create_sensor(new_sen_name, new_sen_type)
    logging.info(f"\nCreated mew sensor {new_sen_name} with type {new_sen_type}")
    sensor_read = sensor_mgr.create_sensor_read_cmd(new_sen_name)
    assert sensor_read.execute() != "", "Unable to read sensor"  # String has content
    logging.info("\nAble to read sensor")
    sensor_mgr.destroy_sensor(new_sen_name)
    logging.info("\nDestroyed sensor")
    logging.info("\nFinished test 3")


def test_sensor_manager_mock_type_register_unregister(sensor_mgr):
    mock = MockSensor("mockSensor")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    assert sensor_mgr.get_supported_sensor_types()[-1] == "mock", "Sensor wasn't registered"
    sensor_mgr.unregister_sensor_type(mock.type())
    assert sensor_mgr.get_supported_sensor_types()[-1] != "mock", "Sensor wasn't unregistered"
    logging.info("\nFinished test")


def test_sensor_manager_mock_sensor_create_destroy(sensor_mgr):
    mock = MockSensor("mockSensor")  # only 1 argument to be called later
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    print("Supported sensor types:", sensor_mgr.get_supported_sensor_types())
    sensor_mgr.create_sensor(mock.name(), 'mock')
    logging.info("\nGetting sensor info:")
    sensors_info = sensor_mgr.get_sensors_info()
    assert sensors_info["mockSensor"] is not None, "Unable to create sensor"
    logging.info(f"\n{sensors_info}")
    sensor_mgr.destroy_sensor(mock.name())
    logging.info("\nDestroyed sensor")
    sensors_info = sensor_mgr.get_sensors_info()
    with pytest.raises(KeyError) as exception_info:
        sensors_info["mockSensor"]
    assert str(exception_info.value) == '\'' + "mockSensor" + '\''
    sensor_mgr.unregister_sensor_type(mock.type())
    logging.info("\nFinished test 5")


def test_sensor_manager_mock_sensor_read_command(sensor_mgr):
    mock = MockSensor("mockSensor")
    sensor_mgr.register_sensor_type(mock.type(), MockSensor)
    sensor_mgr.create_sensor(mock.name(), mock.type())
    sensor_mgr.get_sensors_info()
    sensor_read = sensor_mgr.create_sensor_read_cmd(mock.name())
    sensor_read.execute()
    sensor_was_read = mock.assert_read()
    print(sensor_mgr.sensors["mockSensor"])
    print(sensor_was_read)
    print(f"mock.read_counter: {mock._read_counter}")
    sensor_mgr.destroy_sensor(mock.name())
    logging.info("\nDestroyed sensor")
    sensor_mgr.unregister_sensor_type(mock.type())
    logging.info("\nFinished test 6")
>>>>>>> origin/robin_personal
