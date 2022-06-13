/*
 * This is the REP socket server program for the zmq_req_client script (@ examples/python/zmq_demo).
 * It relies on a pthread to process the socket messages.
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <errno.h>
#include <czmq.h>

/* Message types to set in the test_msg_req type field */
enum test_msg_type {
  TEST_MSG_TYPE_A,
  TEST_MSG_TYPE_B,
  TEST_MSG_TYPE_C,
  TEST_MSG_TYPE_MAX,
};

/* Message request structure */
struct test_msg_req {
    uint8_t type;
    uint32_t val;
} __attribute__((packed));

//https://developer.arm.com/documentation/dui0491/i/Compiler-specific-Features/--attribute--packed---type-attribute?lang=en

/* Message response structure */
struct test_msg_rep {
    uint64_t val_a;
    uint8_t val_b;
} __attribute__((packed));

/* Server thread data */
struct server_data {
    pthread_t tid;
    zsock_t *server;
};

void* msg_server_fn(void *arg)
{
    int ret;
    struct server_data *rdata = arg; //recieves pointer to server_data
    printf("Pointer value: %p of rdata\n", rdata);
    printf("Thread %ld started\n", rdata->tid); // prints long int

    rdata->server = zsock_new(ZMQ_REP); // rdata es puntero?
    // en el puntero de zsock_t server guardamos un nuevo zsock llamado
    //ZMQ_REP
    //no es un objeto entonces qué es?

    zsock_bind(rdata->server, "tcp://localhost:5555");
    //tendremos el server escuchando el cualquier dirección puerto 5555?

    /* Loop processing messages while CZMQ is not interrupted */
    while (!zsys_interrupted) { // ctrl C ?
        zframe_t *req_frame, *rep_frame;
        struct test_msg_req *req;
        struct test_msg_rep *rep;

        // Block waiting for a new message frame
        req_frame = zframe_recv(rdata->server);
        if (!req_frame) {
            fprintf(stderr, "req_frame is NULL\n");
            goto out;
        }
        req = (struct test_msg_req *)zframe_data(req_frame);
        //al frame leído pasado por al función zframe_data 
        //no nulo le hacemos casting a un puntero
        //de test_msg_req y lo ponemo en req
        //qué hace zframe_data
        // cómo sabe que el frame es de 5 bytes

        printf("Received request [type: %hhu, val: %u]\n",
               req->type, req->val);
               // hhu unsigned char
               // u unsigned int

        // rdata->server->

        rep_frame = zframe_new(NULL, sizeof(struct test_msg_rep));
        // guardamos puntero de nuevo zframe creado con NULL y 72 bits
        // en rep_frame
        // buscar primer argumetno de zframe_new en docs

        rep = (struct test_msg_rep *)zframe_data(rep_frame);

        // Write response data
        rep->val_a = req->val + 10;
        rep->val_b = req->val * req->type; //?? multiplica int * char?

        // No longer need request frame
        zframe_destroy(&req_frame); //es como un free
        //le damos posición de memoria de estructura req_frame
        //para que sea borrada

        // Sending destroys the response frame
        ret = zframe_send(&rep_frame, rdata->server, 0);
        //pasamos pos de mem de rep_frame que luego de enviarse
        // también será borrado
        if (ret) { // if mayor a 0 ?
            fprintf(stderr, "Failed to send msg with: %d\n", ret);
            goto out;
        }
    }

out:
    zsock_destroy(&rdata->server); // & da pos de mem?
    // Sí, da posición de memoria del Socket para ser borrado
    // -> es una forma de accesar a la información (variables) desde
    // un puntero, & da la pos de mem de esa variable.
    zsys_interrupted = 1; 
    printf("Thread %ld finished\n", rdata->tid);
    return NULL;
}

int main(int argc, char **argv)
{
    int ret;
    struct server_data rdata = {};
    const uint32_t sleep_ms = 1000;

    // & ptr qué me da?

    ret = pthread_create(&(rdata.tid), NULL, &msg_server_fn, &rdata);
    // revisar pthread_create en docs para entender argumentos
    if (ret != 0) {
        fprintf(stderr, "Failed to create thread :[%s]", strerror(ret));
        return ret;
    }
    /* zsys_interrupted is a global variable from the czmq library that is set
     * when the process receives an interrupt signal (SIGINT). This logic
     * is to stop the program, for example, when the user sends a keyboard
     * interrupt (Ctrl-C).
     */
    while(!zsys_interrupted) {
        zclock_sleep(sleep_ms);
    }
    /* We need some mechanism to stop the server thread that is likely blocked
     * waiting on I/O (new message). Pthread kill sends a signal to a specific thread,
     * which is used to interrupt the blocking zframe_recv call that waits for
     * a new message. When zframe_recv is interrupted it returns a NULL frame, which
     * we detect to break out of the thread's infinite loop.
     *
     * NOTE: An alternative, and maybe safer, approach would be to use a zpoller
     * with a timeout to avoid blocking the server thread indefinitely,
     * plus a stop boolean flag to break out of the while loop. We could
     * also use a high-level CZMQ threaded mechanism (like zloop) to process messages,
     * but that would defeat the purpose of this example (to use pthread) */
    pthread_kill(rdata.tid, SIGINT);
    pthread_join(rdata.tid, NULL);

    return 0;
}
