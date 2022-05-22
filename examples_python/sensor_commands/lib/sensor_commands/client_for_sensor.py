"""
Basic REST API client example using requests.
"""

import sys
import requests
import functools
import json.decoder
from pprint import pformat


def main():
    default_url = 'http://127.0.0.1:8000'
    sys_url = sys.argv[1] if (len(sys.argv) >= 2) else None #**** preguntar    
    url = sys_url or default_url # definir varialbe url, nuestro hostname

    print(url)
    print("######################################################")

    wait_enter = functools.partial(input, "Hit Enter ") #espera un enter, define función

    def pprint_response(resp): # imprimir json y si no sirve impresión tira error
        print(resp)# me tira códigos de estado http
        try:
            print(pformat(resp.json()), "\n")# por qué al poner .json tira toda la info, sino solo código http?
        except json.decoder.JSONDecodeError as e:
            print(e)

    #print("Apioooo:")
    #wait_enter()
    #resp = requests.get(f"{url}")
    #pprint_response(resp)

    """
    @app.post("/devices/") listo
    @app.patch("/devices/") listo
    @app.get("/devices/") listo, param
    @app.get("/devices/{device_name}") listo
    @app.delete("/devices/{device_name}") listo
    @app.put("/command/{device_name}")
    """

    print("Get current devices (GET basic):")#Sirve
    wait_enter() #función definida antes, que espera enter
    device_name = "humidity"
    resp = requests.get(f"{url}/devices/{device_name}")# le añadimos al host name este path, y hace una llamada HTTP get, guarda resultado
    #en json en resp
    #equivalente a str.format(), simplemente más simplificado, reemplaza valor de variable
    #entre {} en un string
    pprint_response(resp) # función previamente definida, imprimir contenido de json

    print("Get current devices with filter (GET with query):")#Sirve
    wait_enter()
    query = {'first': 2, 'limit': 4} # definirmos un diccionario, cuenta empieza en 0
    resp = requests.get(f"{url}/devices/", params=query)# me va a filtar entre resultado en pos 1 (segundo) y pos 3 (cuarto)
    #poner param para un query
    pprint_response(resp)

    print("Create new device (POST):")
    wait_enter()
    new_device = { # deifnir un diccionario de un nuevo objeto, no lo pone en orden, xq no es necesario
        'name': "monitor",
        'description': "LED 4K monitor",
        'price': 1500,
    }
    resp = requests.post(f"{url}/devices/", json=new_device)# va a guardar nuevo objeto, poner json
    pprint_response(resp)# resp es lo que uno envio en json

    #print("Get created device (GET with path param):")
    #wait_enter()
    #resp = requests.get(f"{url}/devices/monitor")#pide path particular
    #pprint_response(resp)

    print("Get current devices again:")
    wait_enter()
    resp = requests.get(f"{url}/devices/")
    pprint_response(resp)

    print("Destroy created device (DELETE with path param):")
    wait_enter()
    resp = requests.delete(f"{url}/devices/{device_name}")# poner path de archivo que quiero borrar
    # me retorna nada, por eso imprime un None tras borrarlo
    pprint_response(resp)

    print("Try to get deleted device again:")
    wait_enter()
    resp = requests.get(f"{url}/devices/{device_name}")# el códido se cae ya que ese path no existe
    pprint_response(resp)

    print("Modify device PATCH:")# da 422???
    wait_enter()
    resp = requests.patch(f"{url}/devices/", json=new_device)# el códido se cae ya que ese path no existe
    pprint_response(resp)

    print("Send command PUT:")# da 405???
    wait_enter()
    resp = requests.put(f"{url}/devices/{device_name}")# el códido se cae ya que ese path no existe
    pprint_response(resp)


if __name__ == "__main__":
    main()