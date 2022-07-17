#ifndef eieDevice_H_
#define eieDevice_H_

/**
 * Starts the comunication client - eieDevice
 * 
 * eie_device_start is in charge of supscribing to the topic 
 * and begin the communication.
 * 
 * @return Pointer to the topic 
 */
void eie_device_start();

/**
 * Stop the comunication
 * 
 * eie_device_stop is in charge of unsubcribe the topic.
 */
void eie_device_stop();

/**
 * eie_device_status_publish is in charge of generating a CJSON 
 * that is going to be send to Ditto.
 * 
 * @param eD EieDevice structure 
 * @param message Message that wants to be send
 */
void eie_device_status_publish(struct eieDevice *eD, const char *message);

/**
 * eie_device_config_handler_register save the function in
 * a Hash table.
 * 
 * @param function pointer to function
 * @param name_feature name of the feature associated
 */
void eie_device_config_handler_register(void *, const char *name_feature);

/**
 * eie_device_create is in charge of generate the struct of eieDevice.
 * 
 * @return struct eieDevice* 
 */
struct eieDevice *eie_device_create(void);


/**
 * eie_device_destroy is in charge of destroying the struct
 * of eieDevice when is not longer needed.
 * 
 * @param eD struct of eieDevice
 */
void eie_device_destroy(struct eieDevice *eD);

#endif // eieDevice_H_