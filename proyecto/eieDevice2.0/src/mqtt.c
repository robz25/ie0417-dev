#include "mqtt.h"

#include <testutil/rand_gen.hpp>



int msg_arrived_cb(void *context, char *topicName, int topicLen, MQTTCLient_message *message){
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