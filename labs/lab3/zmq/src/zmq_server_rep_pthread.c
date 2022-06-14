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

/* Message payload_sizes to set in the test_msg_req payload_size field */
enum test_msg_payload_size {
  TEST_MSG_payload_size_A,
  TEST_MSG_payload_size_B,
  TEST_MSG_payload_size_C,
  TEST_MSG_payload_size_MAX,
};

/* Message request structure */
struct test_msg_req1 {
    uint8_t payload_size;
    uint32_t command_name;
} __attribute__((packed));

/* Message request structure */
struct test_msg_req {
    char command_name[100];
    u_int32_t payload_size;
} __attribute__((packed));

/* Message response structure */
struct test_msg_rep1 {
    uint64_t command_name_rep;
    uint8_t payload_size_rep;
} __attribute__((packed));

/* Message response structure */
struct test_msg_rep {
    char command_name_rep[100];
    u_int32_t payload_size_rep;
    char *payload;
} __attribute__((packed));

/* Server thread data */
struct server_data {
    pthread_t tid;
    zsock_t *server;
};

void* msg_server_fn(void *arg)
{
    int ret;
    struct server_data *rdata = arg;
    printf("Thread %ld started\n", rdata->tid);

    rdata->server = zsock_new(ZMQ_REP);
    zsock_bind(rdata->server, "tcp://*:5555");

    /* Loop processing messages while CZMQ is not interrupted */
    while (!zsys_interrupted) {
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
        char *payload = (char *)zframe_data(req_frame);

        //printf("Received request [payload_size: %hhu, command_name: %u]\n",
        //       req->payload_size, req->command_name);
        printf("\nRequest received");

        printf("\nString received [ command_name: %s, payload_size: %d, Payload: %s]\n",
               req->command_name, req->payload_size, payload+104);

        // printf("Payload %s\n", (payload+104));
        // 111 i
        // el entero tiene 4 bytes...
        // el nombre termina en 99
        // el entero es de 100 a 103
        // el payload empieza en 104

        //Original
        //rep_frame = zframe_new(NULL, sizeof(struct test_msg_rep));
        //rep = (struct test_msg_rep *)zframe_data(rep_frame);
        //Original
        rep = (struct test_msg_rep *)calloc(1, sizeof(struct test_msg_rep));

        char * hola = payload+104;
        // char * hola2 = req->command_name;
        // Write response data
        // strcpy(rep->command_name_rep, req->command_name);

       
        rep->payload = (char *)malloc(req->payload_size);
        memcpy(rep->command_name_rep, req->command_name, strlen(req->command_name));
        // printf("\nPayload tras malloc: %s", rep->payload);
        memcpy(rep->payload, hola, strlen(hola));
        printf("\nPayload tras memcpy: %s", rep->payload);

        // strcpy(rep->payload, hola);
        //test_msg_rep mensaje_prueba = {req->command_name,sizeof(req->command_name)};
        // rep->command_name_rep = req->command_name;
        // rep->command_name_rep = "cc";//req->command_name;// + 10;
        rep->payload_size_rep = req->payload_size;//'b';//req->command_name;// * req->payload_size;
        // rep->payload_size_rep = 'b';//'b';//req->command_name;// * req->payload_size;

        // No longer need request frame
        zframe_destroy(&req_frame);
        printf("\nTamaño de lo enviado %ld", sizeof(rep->command_name_rep) + strlen(hola) + sizeof(rep->payload_size_rep));
        rep_frame = zframe_new(rep, sizeof(rep->command_name_rep) + strlen(hola) + sizeof(rep->payload_size_rep));
        rep = (struct test_msg_rep *)zframe_data(rep_frame);
        
        // Sending destroys the response frame
        ret = zframe_send(&rep_frame, rdata->server, 0);
        printf("\nString sent [ command_name: %s, payload_size: %d, Payload: %s]\n",
               rep->command_name_rep, rep->payload_size_rep, rep->payload);
        if (ret) {
            fprintf(stderr, "Failed to send msg with: %d\n", ret);
            goto out;
        }
    }

out:
    zsock_destroy(&rdata->server);
    zsys_interrupted = 1;
    printf("Thread %ld finished\n", rdata->tid);
    return NULL;
}

int main(int argc, char **argv)
{
    int ret;
    struct server_data rdata = {};
    const uint32_t sleep_ms = 1000;

    ret = pthread_create(&(rdata.tid), NULL, &msg_server_fn, &rdata);
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