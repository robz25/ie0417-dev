#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <linux/limits.h>

#define NUM_DEVICES 2

#include <eieDevice/version.h>
#include <eieDevice/eieDevice.h>

static int basic_command_experiment(void)
{
    int ret;

    struct CommandRunnerConfig cmd_runner_cfg = {
      .q_max_size = 100,
    };
    struct CommandRunner *cmd_runner = command_runner_create(&cmd_runner_cfg);
    if (cmd_runner == NULL) {
        fprintf(stderr, "Failed to create command runner\n");
        return -1;
    }
    struct Command *msg_cmd = msg_command_create("This is a command test message!\n");
    if (msg_cmd == NULL) {
        fprintf(stderr, "Failed to create message command\n");
        return -1;
    }

    printf("++++++++++ CommandRunner experiment ++++++++++\n");

    ret = command_runner_start(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to start command runner with ret=%d\n", ret);
        return -1;
    }

    for (int i=0; i < 10; i++) {
        ret = command_runner_send(cmd_runner, msg_cmd);
        if (ret) {
            fprintf(stderr, "Failed to send command to command runner with ret=%d\n", ret);
            return -1;
        }
    }

    ret = command_runner_stop(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to stop command runner with ret=%d\n", ret);
        return -1;
    }

    command_destroy(msg_cmd);
    command_runner_destroy(cmd_runner);

    return 0;
}

static int device_command_experiment(const char *cfg_filename)
{
    int ret;
    struct DeviceManagerConfig dmgr_cfg = {};
    struct DeviceManager *dmgr = NULL;
    struct Command *cmd = NULL;

    const char *device_names[NUM_DEVICES] = {
      "airQuality_device",
      "lightLevel_device",
    };

    struct Command *commands[NUM_DEVICES] = {};

    struct CommandRunnerConfig cmd_runner_cfg = {
      .q_max_size = 100,
    };
    struct CommandRunner *cmd_runner = command_runner_create(&cmd_runner_cfg);
    if (cmd_runner == NULL) {
        fprintf(stderr, "Failed to create command runner\n");
        return -1;
    }

    printf("---------- Starting DeviceManager experiment ----------\n");

    ret = command_runner_start(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to start command runner with ret=%d\n", ret);
        return -1;
    }

    dmgr_cfg.cfg_filename = cfg_filename;

    dmgr = device_manager_create(&dmgr_cfg);
    if (dmgr == NULL) {
        fprintf(stderr, "Failed to create device manager\n");
        return -1;
    }

    for (int i=0; i < NUM_DEVICES; i++) {
        const char *name = device_names[i];
        if (strlen(name) == 0) break;

        cmd = device_manager_read_cmd_create(dmgr, name);
        if (cmd != NULL) {
            commands[i] = cmd;
            ret = command_runner_send(cmd_runner, cmd);
            if (ret) {
                fprintf(stderr, "Failed to send command to command runner with ret=%d\n", ret);
                return -1;
            }
        } else {
            printf("Failed to get read command for device with name %s\n", name);
        }
    }

    ret = command_runner_stop(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to stop command runner with ret=%d\n", ret);
        return -1;
    }

    for (int i=0; i < NUM_DEVICES; i++) {
        command_destroy(commands[i]);
        commands[i] = NULL;
    }

    device_manager_destroy(dmgr);
    command_runner_destroy(cmd_runner);

    return 0;
}

int main(int argc, char **argv) {
    int opt;
    int ret = 0;
    const char *version = NULL;
    char cfg_filename[PATH_MAX + 1];

    // Parse cmdline options
    while((opt = getopt(argc, (char *const *)argv, "c:")) != -1) {
        switch(opt) {
            case 'c':
                strncpy(cfg_filename, optarg, PATH_MAX);
                break;
            default :
                (void)fprintf(stderr, "Unknown option -%c\n", opt);
                return -EINVAL;
        }
    }

    // Check library version
    ret = device_commands_version(&version);
    if (ret) return ret;
    printf("lib version: %s\n", version);

    // Experiment with basic commands
    basic_command_experiment();

    // Experiment with device commands
    device_command_experiment(cfg_filename);

    return ret;
}

// This main is to make another test with diferent paramers
int mainTest(int argc, char **argv) {

    int opt;
    int ret = 0;
    const char *version = NULL;
    char cfg_filename[PATH_MAX + 1];

    // Parse cmdline options
    while((opt = getopt(argc, (char *const *)argv, "c:")) != -1) {
        switch(opt) {
            case 'c':
                strncpy(cfg_filename, optarg, PATH_MAX);
                break;
            default :
                (void)fprintf(stderr, "Unknown option -%c\n", opt);
                return -EINVAL;
        }
    }

    // Check library version
    ret = device_commands_version(&version);
    if (ret) return ret;
    printf("lib version: %s\n", version);

    // Experiment with basic commands
    basic_command_experiment();

    // Experiment with device commands
    device_command_experiment(cfg_filename);

    return ret;
}


