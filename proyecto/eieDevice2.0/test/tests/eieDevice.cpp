#include "gtest/gtest.h"

#include <demo_api.h>

#include <eieDevice/eieDevice.h>
#include <testutil/rand_gen.hpp>


class eie_device_fixture : public testing::Test
{
 protected:
    /* Fixture class members, accesible from test functions */
    testutil::rand_gen rng;
    EieDevice* eieDevice;

    /* Fixture class constructor */
    /* NOTE: Using reproducible random value for seed, check
     * explanation in unittest_main.cpp for more details */
    eie_device_fixture()
        : rng(rand())
    {
        std::cout << "eieDevice fixture constructor! "<< std::endl;
        std::cout << "  RNG seed " << rng.get_seed() << std::endl;
    }

    virtual void SetUp() {
        std::cout << "eieDevice fixture SetUp! "<< std::endl;

        /*Create eieDevice in SetUp*/
        EieDeviceConfig cnf;  /* Calling struct from command_runner.h*/
        cnf.q_max_size = rng.get_rnd_u64_range(1,1000); /*Randomize the q_max_size configuration parameter between 1 and 1000*/

        eieDevice = eie_device_create(&cnf);

        ASSERT_NE(eieDevice, nullptr);
        /* NOTE: Both the constructor and SetUp methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }

    virtual void TearDown() {
        std::cout << "Test fixture TearDown! "<< std::endl;

        int ret = eie_device_destroy(eieDevice);
        eieDevice = NULL;

        ASSERT_EQ(ret, 0);

        /* NOTE: Both the destructor and TearDown methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }
};

/** Test create_destroy using a fixture */
TEST_F(eie_device_fixture, create_destroy)
{
    // Verify wrong creation of eieDevice
    eieDevice* device = eie_device_create(NULL);
    ASSERT_EQ(device, nullptr);

    // Verify wrong destroy of eieDevice
    int ret = eie_device_destroy(NULL);
    ASSERT_EQ(ret, -1);
    
    
}
/** Test start_stop using a fixture */
TEST_F(eie_device_fixture, start_stop)
{
    // Verify wrong way to start the eieDevice
    int ret = eie_device_start(NULL);
    ASSERT_EQ(ret, -1);

    // Verify the right way to call the eie_device_start
    ret = eie_device_start(commandRunner);
    ASSERT_EQ(ret, 0);

    // Verify wrong way to call the stop eieDevice
    int ret2 = eie_device_stop(NULL);
    ASSERT_EQ(ret2, -1);

    // Verify the right way to call the eie_device_stop
    ret2 = eie_device_stop(commandRunner);
    ASSERT_EQ(ret2, 0);
}
/** Test command_send_single using a fixture */
TEST_F(eie_device_fixture, command_send_single)
{
    Command* msgCmd = msg_command_create("Test message command");

    // verify right way to start the CommandRunner
    int ret = command_runner_start(commandRunner);
    ASSERT_EQ(ret, 0);

    // Wrong way to send command to CommandRunner
    int ret1 = command_runner_send(NULL, msgCmd);
    ASSERT_EQ(ret1, -1);
    
    int ret2 = command_runner_send(commandRunner, NULL);
    ASSERT_EQ(ret2, -1);

    // Right way to call the command_runner_send
    int ret3 = command_runner_send(commandRunner, msgCmd);
    ASSERT_EQ(ret3, 0);

    // Verify the right way to call the command_runner_stop
    int ret4 = command_runner_stop(commandRunner);
    ASSERT_EQ(ret4, 0);
}

