#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

#include "uthash.h"

#include "MQTTClient.h"
#include "eieDevice.h"
#include <testutil/rand_gen.hpp>
#include <../include/eieDevice/external/uthash.h>

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

    /*{"on", on_eieDevice_create},
    {"off", off_eieDevice_create},
    {"", NULL}*/

};


static int ctor_ht_add(struct eieDevice *eD, struct eieDeviceCtorInfo *info){
    struct eieDeviceConstructor *ctor =
        malloc(sizeof(struct eieDeviceConstructor));
    if (ctor == NULL){
        fprintf(stderr, "Failed to allo te eieDevice ctor for type: %s\n", info->type);
        return -ENOMEM;
    }
    ctor->info = *info;
    HASH_ADD_KEYPTR(hh, eD->ctor_ht, info->type, strlen(info->type), ctor);
    return 0;
};

/**Creates the hash table and populates it with the info of the funtions */
static int ctor_ht_create(struct eieDevice *eD)
{

   int ret;
    cJSON *devices = NULL;
    int num_devices = 0;

    devices = cJSON_GetObjectItem(smgr->cfg_cjson, "devices");
    if (devices == NULL) {
        fprintf(stderr, "Failed to read devices array: %s\n", cJSON_GetErrorPtr());
        return -1;
    }

    // Init head entry for sensor hash table
    smgr->sensor_ht = NULL;

    // Iterate over config array to create devices
    num_devices = cJSON_GetArraySize(devices);
    for(int i = 0; i < num_devices; i++)
    {
        struct Sensor *ssr = NULL;
        cJSON *sensor, *obj;
        char *name, *type;
        sensor = cJSON_GetArrayItem(devices, i);

        // Read type and name from JSON
        obj = cJSON_GetObjectItem(sensor, "type");
        if (obj == NULL) {
            fprintf(stderr, "Failed to read sensor type: %s\n", cJSON_GetErrorPtr());
            return -1;
        }
        type = cJSON_GetStringValue(obj);

        obj = cJSON_GetObjectItem(sensor, "name");
        if (obj == NULL) {
            fprintf(stderr, "Failed to read sensor name: %s\n", cJSON_GetErrorPtr());
            return -1;
        }
        name = cJSON_GetStringValue(obj);

        // Create sensor and add it to hash table
        ssr = sensor_factory_sensor_create(smgr->sf, type, name);
        if (ssr == NULL) {
            fprintf(stderr, "Failed to create sensor with type: %s, name: %s\n",
                    type, name);
            return -1;
        }
        ret = sensor_ht_add(smgr, ssr);
        if (ret) {
            fprintf(stderr, "Failed to add sensor with type: %s, name: %s\n",
                    ssr->info.type, ssr->info.name);
            return ret;
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

static int msg_arrived_cb(void *context, char *topicName, int topicLen, MQTTCLient_message *message){

    char* payload;
    fprintf("Message arrived\n");
    fprintf(" topic: %s/n",topicName);
    fprintf("message:");
    payload =(char *)message->payload;
    for(int i=0; i < message ->payloadlen; i++){
        putchar(*payload++);
    }
    putchar('\n');
    MQTTCLient_freeMessage(&message);
    MQTTClient_free(topicName);
    return 1;

};


int eie_device_start(struct eieDevice *eD){
    int ret = 0;
    const char topic[STR_MAX_SIZE] ="EJEMPLO";
    char msg[STR_MAX_SIZE];

    ret = MQTTClient_subscribe(eD, topic, QOS);
};

int eie_device_stop(struct eieDevice *eD){
    int ret = 0;
    ret = MQTTClient_disconnect(eD, 10000);
};


// Se encarga de generar un cJSON para enviarlo a Ditto
int eie_device_status_publish(struct eieDevice *eD, char message){
    int ret = 0;
    MQTTClient_deliveryToken token;
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    const char topic[STR_MAX_SIZE] = "example/test";
    char msg[STR_MAX_SIZE];

    int num_a = (int)rng.get_rnd_u64();
    int num_b = (int)rng.get_rnd_u64();

    ret = snprintf(msg, STR_MAX_SIZE, "Hello!: Num A: %d, Num B: %d", num_a, num_b);
    ASSERT_GT(ret, 0);

    pubmsg.payload = msg;
    pubmsg.payloadlen = strlen(msg);
    pubmsg.qos = QOS;
    pubmsg.retained = 0;

    ret = MQTTClient_publishMessage(client, topic, &pubmsg, &token);
    ASSERT_EQ(ret, MQTTCLIENT_SUCCESS) << "Failed to publish, ret: " << ret << std::endl;

    printf("Waiting for up to %d seconds for publication of message\n"
            "on topic %s for client with ClientID: %s\n",
            (int)(TIMEOUT/1000), topic, CLIENTID);

    ret = MQTTClient_waitForCompletion(client, token, TIMEOUT);
    ASSERT_EQ(ret, MQTTCLIENT_SUCCESS);

    printf("Message with delivery token %d delivered\n", token);
};


typedef int (*eie_config_handler_fn)(void *data);

int eie_device_config_handler_register(struct eieDevice *eD, eie_config_handler_fn func, const char *name_feature){
    
    malloc(sizeof(func));
    if (fun == NULL){
        fprintf(stderr, "Failed to allocate function for type:%s \n", name_feature);
        return -ENOMEM;
    }
    HASH_ADD_KEYPTR(hh,eD->Funtion_fun, name_feature->type, strlen(name_feature->type), Function);
    return 0;
    
};

int eie_device_destroy(struct eieDevice *eD){
    ctor_ht_destroy(eD);
    free(eD);
};
