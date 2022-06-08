#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

#include <sensor_commands/external/uthash.h>
#include "factory.h"
#include "level.h"
#include "temp.h"

typedef struct Command * (*command_create_fn)(const char *name);

/** Command constructor information structure */
struct CommandCtorInfo {
    const char *type;
    command_create_fn create_fn;
};

/** Command constructor structure */
struct CommandConstructor {
    struct CommandCtorInfo info;
    UT_hash_handle hh;
};

/** Command factory structure */
struct CommandFactory {
    /** Head entry for the constructor hash table */
    struct CommandConstructor *ctor_ht;
};

/** Global array with the supported command constructors info */
static struct CommandCtorInfo ctors_info[] = {
  {"message", message_command_create},
  {"ping_pong", ping_pong_command_create},
  {"", NULL},
};

/** Add constructor to the factory's hash table */
static int ctor_ht_add(struct CommandFactory *cf, struct CommandCtorInfo *info)
{
    struct CommandConstructor *ctor =
        malloc(sizeof(struct CommandConstructor));
    if (ctor == NULL) {
        fprintf(stderr, "Failed to allocate command ctor for type: %s\n", info->type);
        return -ENOMEM;
    }
    ctor->info = *info;
    HASH_ADD_KEYPTR(hh, cf->ctor_ht, info->type, strlen(info->type), ctor);
    return 0;
}

/** Creates the factory's hash table and populates it with the global array info */
static int ctor_ht_create(struct CommandFactory *cf)
{
    int ret;
    cf->ctor_ht = NULL;

    // Create ctors from info array and add them to hash table
    for (int i=0;; i++) {
        struct CommandCtorInfo *info = &ctors_info[i];
        // The last info struct should have type == ""
        if ((strlen(info->type) == 0) ||
            (info->create_fn == NULL)) break;

        ret = ctor_ht_add(cf, info);
        if (ret) {
            fprintf(stderr, "Failed to add command ctor for type: %s\n", info->type);
            return ret;
        }
    }
    return 0;
}

/** Destroys the factory's constructor hash table */
static void ctor_ht_destroy(struct CommandFactory *cf)
{
    struct CommandConstructor *ctor, *tmp;
    HASH_ITER(hh, cf->ctor_ht, ctor, tmp) {
        HASH_DEL(cf->ctor_ht, ctor);
        free(ctor);
    }
}

struct CommandFactory *command_factory_create(void)
{
    struct CommandFactory *cf =
        (struct CommandFactory *)calloc(1, sizeof(struct CommandFactory));
    if (cf == NULL) {
        fprintf(stderr, "Failed to allocate command factory\n");
        return NULL;
    }
    ctor_ht_create(cf);
    return cf;
}

struct Command *command_factory_command_create(struct CommandFactory *cf,
                                            const char *type, const char *name)
{
    struct CommandConstructor *ctor = NULL;
    HASH_FIND(hh, cf->ctor_ht, type, strlen(type), ctor);
    if (ctor == NULL) {
        fprintf(stderr, "Command ctor not found for type: %s\n", type);
        return NULL;
    }
    return ctor->info.create_fn(name);
}

void command_factory_destroy(struct CommandFactory *cf)
{
    ctor_ht_destroy(cf);
    free(cf);
}
