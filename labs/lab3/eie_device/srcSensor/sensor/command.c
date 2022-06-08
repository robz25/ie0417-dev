#include <stdio.h>
#include <stdlib.h>

#include <sensor_commands/sensor/sensor.h>

struct Command *command_create(struct CommandInfo *info,
                             struct CommandOps *ops,
                             void *priv)
{
    struct Command *ssr =
        (struct Command *)calloc(1, sizeof(struct Command));
    if (ssr == NULL) {
        fprintf(stderr, "Failed to allocate command\n");
        return NULL;
    }
    ssr->info = *info;
    ssr->ops = ops;
    ssr->priv = priv;
    return ssr;
}

double command_read(struct Command *ssr)
{
    double val = 0;
    if (ssr->ops && ssr->ops->read) {
        val = ssr->ops->read(&ssr->info, ssr->priv);
    }
    return val;
}

void command_destroy(struct Command *ssr)
{
    free(ssr);
}
