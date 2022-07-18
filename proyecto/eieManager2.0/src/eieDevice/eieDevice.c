#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

#include <eieDevice/external/uthash.h>
#include "eieDevice.h"
#define QOS 1
#define STR_MAX_SIZE 100

typedef struct eieDevice * (*eie_device_create)(const char *name);

/** EieDevice constructor information structure */
struct eieDeviceCtorInfo
{
    const char *type;
    eie_device_create create_fn;
};


/** eieDevice constructor structure */
struct eieDeviceConstructor
{
    struct eieDeviceCtorInfo info;
    UT_hash_handle hh;
};

/** eieDevice structure */
struct eieDevice
{
    /** Entry for the constructor hash table */
    struct eieDeviceConstructor *ctor_ht;
};


/** Definirlo bien en nuestro caso, se guardarian las funciones para
 * el eie_Device_handler_register */
/** Global array with the info of the eieDevice constructors*/
static struct eieDeviceCtorInfo ctors_info[] ={
    {"on", on_eieDevice_create},
    {"off", off_eieDevice_create},
    {"", NULL}
};


/** Add constructor to the factory's hash table*/
static int ctor_ht_add(struct eieDevice *eD, struct eieDeviceCtorInfo *info){
    struct eieDeviceConstructor *ctor =
        malloc(sizeof(struct eieDeviceConstructor));
    if (ctor == NULL){
        fprintf(stderr, "Failed to allocate eieDevice ctor for type: %s\n", info->type);
        return -ENOMEM;
    }
    ctor->info = *info;
    HASH_ADD_KEYPTR(hh, eD->ctor_ht, info->type, strlen(info->type), ctor);
    return 0;
};

/**Creates the hash table and populates it with the info of the funtions */
static int ctor_ht_create(struct eieDevice *eD)
{
    int data;
    eD -> ctor_ht = NULL;

    // Create ctors from info array and add them to de Hash Table
    for(int i = 0; ; i++){
        struct eieDeviceCtorInfo *info = &ctors_info[i];
        
        if((strlen(info->type)==0) || (info->create_fn == NULL)) break;
        data = ctor_ht_add(eD, info);
        if (data){
            fprintf(stderr, "Failed to add function ctor fr type: %s\n", info->type);
            return data;
        }
    }
    return 0;
};



/**Destroys the eieDevice constructor hash table*/
static void ctor_ht_destroy(struct eieDevice *eD){
    struct eieDeviceConstructor *ctor, *temp;
    HASH_ITER(hh, eD->ctor_ht, ctor, temp){
        HASH_DEL(eD->ctor_ht,ctor);
        free(ctor);
    }
};



void eie_device_start(struct eieDevice *eD){
    int ret = 0;
    const char topic[STR_MAX_SIZE] ="EJEMPLO";
    char msg[STR_MAX_SIZE];

    ret = MQTTClient_subscribe(eD, topic, QOS);
};

void eie_device_stop(struct eieDevice *eD){
    int ret = 0;
    ret = MQTTClient_disconnect(eD, 10000);
};

void eie_device_status_publish(struct eieDevice *eD, char message){
    
};

typedef struct function *Function;

void eie_device_config_handler_register(struct eieDevice *eD, Function fun, const char *name_feature){
    
    malloc(sizeof(fun));
    if (fun == NULL){
        fprintf(stderr, "Failed to allocate function for type:%s \n", name_feature);
        return -ENOMEM;
    }
    HASH_ADD_KEYPTR(hh,eD->Funtion_fun, name_feature->type, strlen(name_feature->type), Function);
    return 0;
    
};

void eie_device_destroy(struct eieDevice *eD){
    ctor_ht_destroy(eD);
    free(eD);
};