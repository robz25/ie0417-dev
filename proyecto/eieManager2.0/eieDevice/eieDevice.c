#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

#include "eieDevice.h"

void eie_device_start(){};

void eie_device_stop(){};

void eie_device_status_publish(struct eieDevice *eD, const char *message){};

void eie_device_config_handler_register(void *, const char *name_feature){};

struct eieDevice *eie_device_create(void){};

void eie_device_destroy(struct eieDevice *eD){

    free(eD);
};