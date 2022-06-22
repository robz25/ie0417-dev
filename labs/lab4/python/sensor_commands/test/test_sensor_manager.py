
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