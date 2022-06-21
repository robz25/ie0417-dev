# from pytest import fixture
from utils import rand_gen
# import logging
# import demo_api
# from sensor_commands.sensor import Sensor


class DemoFixtureContext:
    def __init__(self):
        self.value = 2
        self.rng = rand_gen.RandomGenerator()

# Cuando llamo el sensor manager creo el objeto de esta clase


"""


class MockSensor(Sensor):  # no tengo que instanciarla

    def assert_read(self) -> bool:
        assert self.read_counter is True  # asi se pone no ==
        self.read_counter = False

    # @abstractmethod
    def read(self) -> float:
        Reads the sensor.
        :return: Sensor reading.
        self.read_counter = True

        return 0.1234  # self.read_counter
"""

"""
aca creo instancia de sensor manager
y creo fixture que retorne sensor manager


@fixture
def demo_ctx_1(example_mod_fixt, example_func_fixt):
    logging.info("Fixture 1 setup!")
    logging.info(f"example_mod_fixt: {example_mod_fixt}")
    logging.info(f"example_func_fixt: {example_func_fixt}")
    ctx = DemoFixtureContext()
    return ctx


@fixture
def demo_ctx_2(example_mod_fixt, example_func_fixt):
    logging.info("Fixture 2 setup!")
    logging.info(f"example_mod_fixt: {example_mod_fixt}")
    logging.info(f"example_func_fixt: {example_func_fixt}")
    ctx = DemoFixtureContext()
    yield ctx
    # NOTE: We return here after the test function finishes
    logging.info("Fixture 2 teardown!")


def test_demo_api_add_random(demo_ctx_1):
    rand_nums = demo_ctx_1.rng.get_unique_int_list(low=1, high=100, num=2)
    assert len(rand_nums) == 2, "Unexpected list length"
    assert all(e >= 1 and e <= 100 for e in rand_nums), "Out of range value in list"

    num_a, num_b = rand_nums
    logging.info(f"  Num A: {num_a}")
    logging.info(f"  Num B: {num_b}")

    r = demo_api.add(num_a + demo_ctx_1.value, num_b)
    logging.info(f"Add result: {r}")

    assert r == num_a + demo_ctx_1.value + num_b, "Addition failed"


def test_demo_api_mult_random(demo_ctx_2):
    rand_nums = demo_ctx_2.rng.get_unique_int_list(low=1, high=100, num=2)
    assert len(rand_nums) == 2, "Unexpected list length"
    assert all(e >= 1 and e <= 100 for e in rand_nums), "Out of range value in list"

    num_a, num_b = rand_nums
    logging.info(f"  Num A: {num_a}")
    logging.info(f"  Num B: {num_b}")

    r = demo_api.mult(num_a, num_b + demo_ctx_2.value)
    logging.info(f"Mult result: {r}")

    assert r == num_a * (num_b + demo_ctx_2.value), "Multiplication failed"
"""
