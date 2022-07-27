#!/usr/bin/python3

"""
Basic REST API client using requests.
"""

import sys
import requests
import functools
import json.decoder
from pprint import pformat

def get_things(url):
    print("Get current things from Ditto REST API (GET digital twins):")  # Sirve
    path_to_call = "/things/"
    print(f"Get request to: {url}{path_to_call}")
    resp = requests.get(f"{url}{path_to_call}")  # le añadimos al host
    # name este path, y hace una llamada HTTP get, guarda resultado en json
    # en resp equivalente a str.format(), simplemente más simplificado,
    # reemplaza valor de variable entre {} en un string
    pprint_response(resp) 


def pprint_response(resp):  # imprimir json y si no sirve impresión tira
     # error
    print(resp)  # me tira códigos de estado http
    try:
        print(pformat(resp.json()), "\n")  # por qué al poner .json tira
         # toda la info, sino solo código http?
    except json.decoder.JSONDecodeError as e:
        print(e)


def main():
    user = "ditto"
    password = "ditto"
    default_url = f'http://{user}:{password}@localhost:8080/api/2'
    sys_url = sys.argv[1] if (len(sys.argv) >= 2) else None  # **** preguntar
    url = sys_url or default_url  # definir varialbe url, nuestro hostname
    options = ["Salir","Mostrar dispositivos","Seleccionar dispositivo","Configurar dispositivo","Leer estado de dispositivo"]
    wait_enter = functools.partial(input, "Hit Enter ")  # espera un enter,
    # define función

    option = -1
    while(option!=0):

        for option in range(len(options)):
            print(f"{option}. {options[option]}\n")
        selection = input("Seleccione una opción\n")
        if(selection=="0"):
            print(0)
            return 0
        elif(selection=="1"):
            get_things(url)
            print(1)
        elif(selection=="2"):
            print(2)
        elif(selection=="3"):
            print(3)
        elif(selection=="4"):
            print(4)

if __name__ == "__main__":
    main()
