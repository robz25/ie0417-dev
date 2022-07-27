#include <stdio.h>
#include <stdlib.h>

#include "airQuality.h"

struct TempDeviceState {
    int value;
};

static double temp_Device_read(struct DeviceInfo *info, void *priv)
{
    struct TempDeviceState *state = priv;
    printf("Reading temp Device with name: %s\n", info->name);
    return state->value;
}

struct DeviceOps temp_Device_ops = {
  .read = temp_Device_read,
};

struct Device * temp_Device_create(const char *name)
{
    struct DeviceInfo info = {};
    struct TempDeviceState *state =
        calloc(1, sizeof(struct TempDeviceState));
    if (state == NULL) {
        fprintf(stderr, "Failed to allocate temp Device state\n");
        return NULL;
    }
    info.type = "temperature";
    info.unit = "celsius";
    info.name = name;
    state->value = 42;

    return Device_create(&info, &temp_sensor_ops, state);
}
