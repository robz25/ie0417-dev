#!/usr/bin/python3



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
    print("\nSending: ",req)
    client.send(req)

def recieveMessage(client):
    rep = client.recv()
    print("\nResponse: ",rep)
    print("\nlargo del rep: ", str(len(rep)))
    command_name, payload_size, payload = struct.unpack("<100sI%ds" %(len(rep)-104), rep)
    print(f"\nReceived response [Command name: {command_name}, payload size: {payload_size}, payload: {payload}]")

def main():
    port = 5555;
    context = zmq.Context()
    print("Connecting to server...")
    client = context.socket(zmq.REQ)
    with client.connect(f"tcp://localhost:{port}"):
        for i in range(1):
            # Send request
            # Assuming little-endian in C side
            
            command_name = "Ping pong" # \00 para terminar el mensaje
            
            payload = {
                "i": "i ",
                "var1": "100pci",
                "var2": "109var ",
            }
            
            sendMessage(client, command_name,payload)

            recieveMessage(client)
            """
            command_name = "Message" # \00 para terminar el mensaje
            
            payload = {
                "1": "Este es el commando message ",
                "2": "Message2",
                "3": "Message3",
            }
            
            
            sendMessage(client, command_name,payload)

            recieveMessage(client)
            """


if __name__ == "__main__":
    main()