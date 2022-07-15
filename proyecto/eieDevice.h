#ifndef eieDevice_H_
#define eieDevice_H_

//#include <>

void eie_device_start();

void eie_device_stop();

void eie_device_status_publish(struct eieDevice *eD, const char *message);

void eie_device_config_handler_register(void, const char *name_feature);
//recibe función y el nombre del feature al que está asociada 

struct eieDevice *eie_device_create(void);


struct create *eie_device_create(struct eieDevice *eD, const char *name, const char *message
);
//creates struct eieDevice

void eie_device_destroy(struct eieDevice *eD);

#endif // eieDevice_H_