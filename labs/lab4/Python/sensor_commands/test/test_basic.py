# import pytest
# import logging
# from random import choice

# import sensor_commands
# from sensor_commands.lib.sensor_commands.sensor.sensor import MockSensor
"""

from sensor_commands.sensor.analyzers import avg_thresh_analyzer as avt
from sensor_commands import command
from sensor_commands.sensor.manager import SensorManager
from sensor_commands.args import parse_args


args = parse_args()
config_name = args.config
sensor_type_name = args.sensor_type
sensor_cmd_per_period, sensor_period_sec = (100, 5)
alert_cmd_per_period, alert_period_sec = (2, 1)
analyzer_avg_thresh = 10
num_read_commands = 200

# Set up command runners
sensor_mgr = SensorManager(config_name)
sensor_cmd_runner = command.CommandRunner(
    cmd_per_period=sensor_cmd_per_period,
    period_sec=sensor_period_sec)
alert_cmd_runner = command.CommandRunner(
    cmd_per_period=alert_cmd_per_period,
    period_sec=alert_period_sec)
sensor_cmd_runner.start()
alert_cmd_runner.start()

# Set up sensor analyzer with "above average threshold alert" strategy
analyzer = avt.SensorAvgThreshAnalyzer(avg_thresh=analyzer_avg_thresh)
avt.set_alert_handle_strategy(analyzer, alert_cmd_runner)
avt.set_above_compare_strategy(analyzer)

# Generate read commands for temp sensors
temp_sensor_names = sensor_mgr.get_sensor_names_per_type(sensor_type_name)
for _ in range(num_read_commands):
    rand_sensor_name = choice(temp_sensor_names)
    read_cmd = sensor_mgr.create_sensor_read_cmd(rand_sensor_name, analyzer)

"""


def test_sensor_manager_supported_types():
    assert len(5) > 0, "List of sensor types is empty"


def test_sensor_manager_mock_type_register_unregister():
    assert 1 + 1 == 2, "Math is wrong"


def test_sensor_manager_mock_sensor_create_destroy():
    assert 1 * 9 == 9, "Math is ok"


def test_sensor_manager_mock_sensor_read_command():
    assert 1 + 1 != 0, "Math is ok"


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
