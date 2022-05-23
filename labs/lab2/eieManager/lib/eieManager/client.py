#!/usr/bin/python3

"""
Basic REST API client using requests.
"""

import sys
import requests
import functools
import json.decoder
from pprint import pformat


def main():
    default_url = 'http://127.0.0.1:8000'
    sys_url = sys.argv[1] if (len(sys.argv) >= 2) else None  # **** preguntar
    url = sys_url or default_url  # definir varialbe url, nuestro hostname

    wait_enter = functools.partial(input, "Hit Enter ")  # espera un enter,
    # define función

    def pprint_response(resp):  # imprimir json y si no sirve impresión tira
        # error
        print(resp)  # me tira códigos de estado http
        try:
            print(pformat(resp.json()), "\n")  # por qué al poner .json tira
            # toda la info, sino solo código http?
        except json.decoder.JSONDecodeError as e:
            print(e)

    """
    @app.post("/devices/") listo
    @app.patch("/devices/") listo
    @app.get("/devices/") listo, param
    @app.get("/devices/{device_name}") listo
    @app.delete("/devices/{device_name}") listo
    @app.put("/command/{device_name}")
    """

    print("Get current devices (GET basic):")  # Sirve
    wait_enter()  # función definida antes, que espera enter
    device_name = "Device-03"
    resp = requests.get(f"{url}/devices/")  # le añadimos al host
    # name este path, y hace una llamada HTTP get, guarda resultado en json
    # en resp equivalente a str.format(), simplemente más simplificado,
    # reemplaza valor de variable entre {} en un string
    pprint_response(resp)  # función previamente definida, imprimir contenido
    # de json

    print("Get current devices with filter (GET with query):")  # Sirve
    wait_enter()
    query = {'first': 1, 'limit': 3}  # definirmos un diccionario, cuenta
    # empieza en 0
    resp = requests.get(f"{url}/devices/", params=query)  # me va a filtar
    # entre resultado en pos 1 (segundo) y pos 3 (cuarto)
    # poner param para un query
    pprint_response(resp)

    print("Create new device (POST):")
    wait_enter()
    new_device = {  # deifnir un diccionario de un nuevo device, no lo pone en
            # orden, xq no es necesario
            "name": "Device-07",
            "type": "Level",
            "commands": "Status",  # can't send lists, but a str with a list
            "ip": "192.168.0.077:8001",
        }
    resp = requests.post(f"{url}/devices/", json=new_device)  # va a guardar
    # nuevo objeto, poner json
    pprint_response(resp)

    print("Create another new device (POST):")
    wait_enter()
    new_device = {  # deifnir un diccionario de un nuevo device, no lo pone en
            # orden, xq no es necesario
            "name": "Device-08",
            "type": "Sensor",
            "commands": "Measure",  # can't send lists, but a str with a list
            "ip": "192.123.0.333:8333",
        }
    resp = requests.post(f"{url}/devices/", json=new_device)  # va a guardar
    # nuevo objeto, poner json
    pprint_response(resp)

    print("Get current devices again:")
    wait_enter()
    resp = requests.get(f"{url}/devices/")
    pprint_response(resp)

    print("Destroy created device (DELETE with path param):")
    wait_enter()
    device_to_destroy = "Device-08"
    resp = requests.delete(f"{url}/devices/{device_to_destroy}")  # poner path de
    # archivo que quiero borrar me retorna nada, por eso imprime un None tras
    # # borrarlo
    pprint_response(resp)

    print("Try to get deleted device will get 500:")
    wait_enter()
    resp = requests.get(f"{url}/devices/{device_to_destroy}")  # el códido se cae ya
    # que ese path no existe
    pprint_response(resp)

    print("Modify device PATCH:")  # sirve
    wait_enter()
    patch_device = {  # deifnir un diccionario de un nuevo device, no lo pone en
            # orden, xq no es necesario
            "name": "Device-07",
            "type": "Level",
            "commands": "Hola",  # can't send lists, but a str with a list
            "ip": "172.180.0.111:5555",
        }
    resp = requests.patch(f"{url}/devices/", json=patch_device)  # el códido se
    # cae ya que ese path no existe
    pprint_response(resp)

    print("Get current devices again:")
    wait_enter()
    resp = requests.get(f"{url}/devices/")
    pprint_response(resp)

    # (command, device, arg1=val1, ..., argN=valN)
    print("Send command PUT:")
    wait_enter()
    new_command = {
            "device_name": "Device-07",
            "command": "Status",
            "args": "last_start"
        }
    resp = requests.put(f"{url}/command/", json=new_command)  # send command 
    # in json with device name
    pprint_response(resp)


if __name__ == "__main__":
    main()
