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

    virtual void SetUp() {
        std::cout << "Command Runner fixture SetUp! "<< std::endl;

        /*Create CommandRunner in SetUp*/
        struct CommandRunnerConfig cmdR  ;  /* Calling struct from command_runner.h*/
        cmdR.q_max_size = rand()*999+1;  /*Randomize the q_max_size configuration parameter between 1 and 1000*/
        CommandRunner* commandRunner = command_runner_create(&cmdR);

        /* NOTE: Both the constructor and SetUp methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }

    virtual void TearDown() {
        std::cout << "Test fixture TearDown! "<< std::endl;

        void command_runner_destroy(CommandRunner)


        /* NOTE: Both the destructor and TearDown methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }
};

/** Test create_destroy using a fixture */
TEST_F(command_runner, create_destroy)
{
    int ret = 0;
    int ret2 = 0;
    

    struct command_runner_create (NULL cfg);
        if (command_runner_create.cmd_runner != 0){
            ret = demo_api_result(NULL);
        }    

    void command_runner_destroy(CommandRunner);  /* Should be with NULL cmd_runner */
        if (command_runner_destroy != 0){
            ret2 = demo_api_result('-1');
        } 

    ASSERT_EQ(ret, DEMO_API_OK);
    ASSERT_EQ(ret2, DEMO_API_OK);
    
    
}
/** Test start_stop using a fixture */
TEST_F(command_runner, start_stop)
{
    int ret = 0;
    int ret2 = 0;
    int command_runner_start(CommandRunner NULL);
        if (command_runner_start != 0){
        ret = demo_api_result('-1');
        } 
    int command_runner_stop(CommandRunner NULL);
        if (command_runner_stop != 0){
        ret2 = demo_api_result('-1');
        } 

    ASSERT_EQ(ret, DEMO_API_OK);
    ASSERT_EQ(ret2, DEMO_API_OK);
}

TEST_F(command_runner, command_send_single)
{
    int ret = 0;
    int ret2 = 0;
    int ret3 = 0;
    int command_runner_send(CommandRunner NULL);
        if (command_runner_start != 0){
        ret = demo_api_result('-1');
        } 
    int command_runner_send(CommandRunner msg_command);
        if (command_runner_stop != 0){
        ret2 = demo_api_result('-1');
        } 
        else {
             ret2 = demo_api_result('Is correct!');
        }
    int command_runner_stop(CommandRunner NULL);
        if (command_runner_stop != 0){
        ret3 = demo_api_result('-1');
        } 
        else {
             ret3 = demo_api_result('Is correct!');
        }

    ASSERT_EQ(ret, DEMO_API_OK);
    ASSERT_EQ(ret2, DEMO_API_OK);
    ASSERT_EQ(ret3, DEMO_API_OK);
