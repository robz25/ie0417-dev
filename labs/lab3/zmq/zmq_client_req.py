#!/usr/bin/python3

"""
PyZMQ REQ socket client example module.

This is the client script for the zmq_server_rep_pthread program (@ examples/c/zmq_demo).
"""

import time
import zmq
import struct
import json  # to convert dictionary to json

def sendMessage(client, command_name, payload):
    command_name = command_name.ljust(100)
    command_name = command_name.encode('utf-8')
    payload_json = json.dumps(payload)
    payload_size = len(payload_json)
    payload_json = payload_json.encode('utf-8')
    req = struct.pack("%dsI%ds" %(len(command_name),len(payload_json)), command_name, payload_size, payload_json) # I para entero sin signo de 32 bits
    print("Sending: ",req)
    client.send(req)

def main():
    port = 5555;
    context = zmq.Context()
    print("Connecting to server...")
    client = context.socket(zmq.REQ)
    with client.connect(f"tcp://localhost:{port}"):
        for i in range(10):
            # Send request
            # Assuming little-endian in C side
            
            command_name = "43hola yeah sirve" # \00 para terminar el mensaje
            # command_name = command_name.ljust(100)
            # req_type = req_type.encode('utf-8')
            # command_name = command_name.encode('utf-8')
            # s = "holi\00"
            # s = s.encode('utf-8')
            payload = {
                "i": "i ",
                "var1": "100pci",
                "var2": "109var ",
            }
            # payload_json = json.dumps(payload)
            # req_type = len(payload_json)
            # payload_json = payload_json.encode('utf-8')
            sendMessage(client, command_name,payload)
            # req = struct.pack('<cs', req_type, command_name)
            # req = struct.pack("I%ds" % (len(s),), len(s), s)
            #req = struct.pack("B%ds" %(len(s)), len(s), s) # working
            # req = struct.pack("%dsI%ds" %(len(command_name),len(payload_json)), command_name, req_type, payload_json) # I para entero sin signo de 32 bits
            # print("Sending: ",req)
            # client.send(req)

            """
            s = bytes(s, 'utf-8')    # Or other appropriate encoding
            struct.pack("I%ds" % (len(s),), len(s), s)
            """
            # Receive response
            rep = client.recv()
            print("\nResponse: ",rep)
            print("Response 0: ",rep[0])
            print("Response 1: ",rep[1])
            print("Response 1: ",rep[2])
            # rep_val_a, rep_val_b = struct.unpack('<QB', rep)
            # rep_val_a, rep_val_b = struct.unpack('<QQ', rep)
            rep_val_a, rep_val_b = struct.unpack('<100sI', rep)
            # rep_val_a = struct.unpack('<c', rep[0])
            # rep_val_b = struct.unpack('<c', rep[1])
            print(f"Received response [val_a: {rep_val_a}, val_b: {rep_val_b}]")


if __name__ == "__main__":
    main()