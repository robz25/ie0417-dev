#include <stdio.h>
#include <stdlib.h>

#include "message.h"

struct MessageCommandState {
    int value;
};


struct Command * message_command_create()
{
    struct CommandInfo info = {};
    struct LevelSensorState *state =
        calloc(1, sizeof(struct LevelSensorState));
    if (state == NULL) {
        fprintf(stderr, "Failed to allocate level sensor state\n");
        return NULL;
    }
    info.type = "command";
    info.unit = "message";
    info.name = 'output';
    state->value = 100;

    return sensor_create(&info);
}
