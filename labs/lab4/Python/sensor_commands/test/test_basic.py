# import logging
# import pytest

# import sensor_commands
# from sensor_commands.lib.sensor_commands.sensor.sensor import MockSensor
# from sensor_commands.lib.sensor_commands.args import parse_args


def test1():
    assert 1 + 1 == 2, "Math is wrong"


"""
def test_sensor_manager_mock_type_register_unregister():
    args = parse_args()
    config_name = args.config
    sensor_mgr_tester = SensorManager(config_name)
    sensor_mgr_tester.register_sensor_type("mock",MockSensor)
    sensor_mgr_tester.get_supported_sensor_types()


def test_demo_api_add_op():
    r = demo_api.add(5, 9)
    logging.info(f"Add result: {r}")
    assert r == 14, "Addition failed!"


def test_demo_api_mult_op():
    r = demo_api.mult(5, 4)
    logging.info(f"Mult result: {r}")
    assert r == 20, "Multiplication failed!"


def test_demo_api_double_if_pos_op():
    r = demo_api.double_if_pos(5)
    logging.info(f"Double result: {r}")
    assert r == 10, "Double failed!"


def test_demo_api_double_if_pos_sanity():
    with pytest.raises(AssertionError):
        demo_api.double_if_pos(-4)
"""
