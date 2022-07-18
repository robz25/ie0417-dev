#ifndef mqtt_H_
#define mqtt_H_


int msg_arrived_cb(void *context, char *topicName, int topicLen, MQTTCLient_message *message);


#endif // mqtt_H_