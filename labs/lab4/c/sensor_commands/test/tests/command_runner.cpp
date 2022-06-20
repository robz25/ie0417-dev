#include "gtest/gtest.h"
#include "include/sensor_commands/command_runner.h"
#include "include/sensor_commands/command.h"
#include <demo_api.h>
#include <testutil/rand_gen.hpp>

/** Example fixture class for demo API tests */
class command_runner : public testing::Test
{
 protected:
    /* Fixture class members, accesible from test functions */
    commandRunner cmdR  ;
    testutil::rand_gen rng;

    /* Fixture class constructor */
    /* NOTE: Using reproducible random value for seed, check
     * explanation in unittest_main.cpp for more details */
    command_runner()
        : rng(rand())
    {
        std::cout << "Command Runner fixture constructor! "<< std::endl;
        std::cout << "  RNG seed " << rng.get_seed() << std::endl;
    }

    virtual void SetUp() override{
        command_runner::SetUp();
        std::cout << "Test fixture SetUp! "<< std::endl;
        /*Create CommandRunner i SetUp    */
        commandRunnerCOnfig = CommandRunnerConfig(rand()*999+1);
        cmdR =command_runner_create(cfg);
        

        /* NOTE: Both the constructor and SetUp methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }

    virtual void TearDown() override{
        std::cout << "Test fixture TearDown! "<< std::endl;

        command_runner::TearDown(); 
        /* NOTE: Both the destructor and TearDown methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }
};

/** Test the addition operation of two random values using a fixture */
TEST_F(command_runner, create_destroy)
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
TEST_F(command_runner, start_stop)
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

TEST_F(command_runner, command_send_single)
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
