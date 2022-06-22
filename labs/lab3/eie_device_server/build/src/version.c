#include <sensor_commands/version.h>

static const char * LIB_VERSION = "0.0.1";

int sensor_commands_version(const char **version) {
    *version = LIB_VERSION;
    return 0;
}
