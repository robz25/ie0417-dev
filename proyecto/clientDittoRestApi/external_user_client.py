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


#PUT /api/2/things/{thingId}/features/temperature/properties/value?condition=ne(features/temperature/properties/value,23.9)
#body: 23.5
def modify_property(url):
   path_to_call = "/things/eielabs:lightingSystem/features/power/properties/configuration?condition=ne(features/power/properties/configuration,\"off\")"
   body = "off"
   resp = requests.post(f"{url}{path_to_call}", data=body)
   pprint_response(resp) 


def reset_devices(url):

   print("Create new device (POST):")
   path_to_call = "/things/"
   
   device1 = {
        "policyId": "eielabs:open_policy",
        "attributes": {
            "name": "Lab Air 1",
            "type": "Air Quality Sensor"
        },
        "features": {
            "air_sensor_ppm": {
                "properties": {
                    "configuration": 0,
                    "status": 105
                }
            },
            "air_sensor_sample_freq_minutes": {
                "properties": {
                    "configuration": 5,
                    "status": 5
                }
            },
                "fan_speed": {
                "properties": {
                    "configuration": 2,
                    "status": 2
                }
            },
            "power":{
                "properties": {
                    "configuration": "on",
                    "status": "on"
                }
            }
        }
    }

   device2 = {
        "policyId": "eielabs:open_policy",
        "attributes": {
            "name": "Main light",
            "type": "Lamp",
        },
        "features": {
            "light_intensity": {
                "properties": {
                    "configuration": 85,
                    "status": 85,
                }
            },
            "light_color": {
                "properties": {
                    "configuration": "bright white",
                    "status": "bright white",
                }
            },
            "timer_minutes": {
                "properties": {
                    "configuration": 15,
                    "status": 14,
                }
            },
            "power":{
                "properties": {
                    "configuration": "on",
                    "status": "on",
                }
            },
        },
    }
    # curl -X PUT 'http://localhost:8080/api/2/things/eielabs:lightingSystem' -u 'ditto:ditto' -H 'Content-Type: application/json' -d '

   path_to_call = "/things/eielabs:lightingSystem"
   resp = requests.post(f"{url}{path_to_call}", json=device1)
   pprint_response(resp) 
   path_to_call = "/things/eielabs:AirQualitySensor"
   resp = requests.post(f"{url}{path_to_call}", json=device2)
   pprint_response(resp)


def main():
    user = "ditto"
    password = "ditto"
    default_url = f'http://{user}:{password}@localhost:8080/api/2'
    sys_url = sys.argv[1] if (len(sys.argv) >= 2) else None  # **** preguntar
    url = sys_url or default_url  # definir varialbe url, nuestro hostname
    options = ["Salir","Mostrar dispositivos","Restablecer dispositivos","Configurar dispositivo"]
    wait_enter = functools.partial(input, "Hit Enter ")  # espera un enter,
    # define función

    option = -1
    while(option!=0):

        for option in range(len(options)):
            print(f"{option}. {options[option]}\n")
        selection = input("Seleccione una opción\n")
        if(selection=="0"):
            return 0
        elif(selection=="1"):
            get_things(url)
        elif(selection=="2"):
            reset_devices(url)
        elif(selection=="3"):
            modify_property(url)
        elif(selection=="4"):
            print(4)

if __name__ == "__main__":
    main()
