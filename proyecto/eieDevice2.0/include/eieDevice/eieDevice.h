#ifndef eieDevice_H_
#define eieDevice_H_


/**
 * EieDevice constructor information structure
 * 
 */
struct eieDeviceCtorInfo
{
    const char *type;
};

/**
 * eie_device_create is in charge of generate the struct of eieDevice.
 *
 * Creates hash table
 *
 * @param cfg  Command runner configuration
 *
 * @return Pointer to a command runner structure.
 */
struct eieDevice * eie_device_create(struct eieDeviceCtorInfo *cfg);



/**
 * Starts the comunication client - eieDevice
 * 
 * eie_device_start is in charge of supscribing to the topic 
 * and begin the communication.
 * 
 * @return Pointer to the topic 
 */
void eie_device_start(struct eieDevice *eD);

/**
 * Stop the comunication
 * 
 * eie_device_stop is in charge of unsubcribe the topic.
 */
void eie_device_stop(struct eieDevice *eD);

/**
 * eie_device_status_publish is in charge of generating a CJSON 
 * that is going to be send to Ditto.
 * 
 * @param eD EieDevice structure 
 * @param message Message that wants to be send
 */
void eie_device_status_publish(struct eieDevice *eD, char message);

/**
 * eie_device_config_handler_register save the function in
 * a Hash table.
 * 
 * @param function pointer to function
 * @param name_feature name of the feature associated
 */
void eie_device_config_handler_register(struct eieDevice *eD, Function fun, const char *name_feature);

/**
 * eie_device_destroy is in charge of destroying the struct
 * of eieDevice when is not longer needed.
 * 
 * @param eD struct of eieDevice
 */
void eie_device_destroy(struct eieDevice *eD);

#endif // eieDevice_H_