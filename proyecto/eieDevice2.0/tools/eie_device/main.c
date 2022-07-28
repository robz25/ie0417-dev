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

    struct eieDeviceConfig eie_device_cfg = {
      .q_max_size = 100,
    };
    struct eieDevice *cmd_runner = eie_device_create(&cmd_runner_cfg);
    if (cmd_runner == NULL) {
        fprintf(stderr, "Failed to create command runner\n");
        return -1;
    }
    struct Device*msg_cmd = eie_device_create("This is a device test message!\n");
    if (msg_cmd == NULL) {
        fprintf(stderr, "Failed to create device command\n");
        return -1;
    }

    printf("++++++++++ eieDevice experiment ++++++++++\n");

    ret = eie_device_start(eieDevice);
    if (ret) {
        fprintf(stderr, "Failed to start eie_device with ret=%d\n", ret);
        return -1;
    }

    for (int i=0; i < 10; i++) {
        ret = eie_device_config_handler_register(eieDevice, msg_cmd);
        if (ret) {
            fprintf(stderr, "Failed to send command to eie device with ret=%d\n", ret);
            return -1;
        }
    }

    ret = eie_device_stop(eieDevice);
    if (ret) {
        fprintf(stderr, "Failed to stop eie device with ret=%d\n", ret);
        return -1;
    }

    command_destroy(msg_cmd);
    command_runner_destroy(eieDevice);

    return 0;
}
