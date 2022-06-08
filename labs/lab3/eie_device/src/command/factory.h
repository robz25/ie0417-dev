#ifndef FACTORY_H_
#define FACTORY_H_

#include <sensor_commands/sensor/sensor.h> /* Cambiarlo 

/**
 * Creates a command factory
 *
 * The command factory is in charge of abstracting the construction
 * of different types of commands. The correct command type is going
 * to be instantiated internally according to the desired type
 * and the generic command structure is returned.
 *
 * @return Pointer to a command factory structure.
 */
struct CommandFactory *command_factory_create(void);

/**
 * Creates a command according to the factory logic
 *
 * @param cf   Command factory structure.
 * @param type Command type to be created.
 * @param name Name of the command to create.
 *
 * @return Pointer to a command factory structure.
 */
struct Command *command_factory_command_create(struct CommandFactory *cf,
                                            const char *type, const char *name);

/**
 * Destroys the command factory
 *
 * @param cf Command factory structure.
 */
void command_factory_destroy(struct CommandFactory *cf);

#endif // FACTORY_H_
