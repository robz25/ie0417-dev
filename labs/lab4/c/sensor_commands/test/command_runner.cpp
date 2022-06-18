#include "gtest/gtest.h"
#include <demo_api.h>
#include <testutil/rand_gen.hpp>

int main(int argc, char *argv[]) {
    int init_seed = 0;
    ::testing::InitGoogleTest(&argc, argv);

    /* NOTE: We will use cstdlib rand() to get the seeds for the
     * C++ pseudo-random number generators (RNGs). This sets the
     * initial seed with value from --gtest_random_seed via srand(),
     * to get reproducible seed values with rand() */
    init_seed = ::testing::GTEST_FLAG(random_seed);
    if (init_seed == 0) {
        init_seed = time(NULL);
    }
    std::cout << "Random seed: " << init_seed << std::endl;
    srand(init_seed);

    return RUN_ALL_TESTS();
}

/** Example fixture class for demo API tests applied to command_runner test */
class command_runner: public testing::Test
{
 protected:
    /* Fixture class members, accesible from test functions */
    int value;
    testutil::rand_gen rng;

    /* Fixture class constructor */
    /* NOTE: Using reproducible random value for seed, check
     * explanation in unittest_main.cpp for more details */
    command_runner()
        : value(2), rng(rand())
    {
        std::cout << "Test fixture constructor! "<< std::endl;
        std::cout << "  RNG seed " << rng.get_seed() << std::endl;
    }

    virtual void SetUp() {
        std::cout << "Test fixture SetUp! "<< std::endl;
        /* NOTE: Both the constructor and SetUp methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }

    virtual void TearDown() {
        std::cout << "Test fixture TearDown! "<< std::endl;
        /* NOTE: Both the destructor and TearDown methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }
};

/** Test the addition operation of two random values using a fixture */
TEST_F(demo_api_fixture, add_random)
{
    int ret = 0;
    int out = 0;
    int num_a = (int)rng.get_rnd_u64();
    int num_b = (int)rng.get_rnd_u64();
    std::cout << "  Num A: " << num_a << std::endl;
    std::cout << "  Num B: " << num_b << std::endl;

    ret = demo_api_add(num_a + value, num_b, &out);
    ASSERT_EQ(ret, DEMO_API_OK);
    ASSERT_EQ(out, num_a + value + num_b);
}

/** Test the multiplication operation of two random values using a fixture */
TEST_F(demo_api_fixture, mult_random)
{
    int ret = 0;
    int out = 0;
    int num_a = (int)rng.get_rnd_u64();
    int num_b = (int)rng.get_rnd_u64();
    std::cout << "  Num A: " << num_a << std::endl;
    std::cout << "  Num B: " << num_b << std::endl;

    ret = demo_api_mult(num_a, num_b + value, &out);
    ASSERT_EQ(ret, DEMO_API_OK);
    ASSERT_EQ(out, num_a * (num_b + value));
}

