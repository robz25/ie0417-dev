#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <linux/limits.h>

#include <eieDevice.h>


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
    ret = sensor_commands_version(&version);
    if (ret) return ret;
    printf("lib version: %s\n", version);

    // Experiment with basic commands
    basic_command_experiment();

    // Experiment with sensor commands
    sensor_command_experiment(cfg_filename);

    return ret;
}

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
    ret = sensor_commands_version(&version);
    if (ret) return ret;
    printf("lib version: %s\n", version);

    // Experiment with basic commands
    basic_command_experiment();

    // Experiment with sensor commands
    sensor_command_experiment(cfg_filename);

    return ret;
}
