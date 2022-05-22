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

    print("Apioooo:")
    wait_enter()
    resp = requests.get(f"{url}")
    pprint_response(resp)

"""
@app.post("/sensors/") listo
@app.patch("/sensors/") listo
@app.get("/sensors/") listo, param
@app.get("/sensors/{sensor_name}") listo
@app.delete("/sensors/{sensor_name}") listo
@app.put("/command/{sensor_name}")
"""

    print("Get current sensors (GET basic):")
    wait_enter() #función definida antes, que espera enter
    sensor_name = "humidity"
    resp = requests.get(f"{url}/sensors/{sensor_name}")# le añadimos al host name este path, y hace una llamada HTTP get, guarda resultado
    #en json en resp
    #equivalente a str.format(), simplemente más simplificado, reemplaza valor de variable
    #entre {} en un string
    pprint_response(resp) # función previamente definida, imprimir contenido de json

    print("Get current sensors with filter (GET with query):")
    wait_enter()
    query = {'first': 1, 'limit': 3} # definirmos un diccionario, cuenta empieza en 0
    resp = requests.get(f"{url}/sensors/", params=query)# me va a filtar entre resultado en pos 1 (segundo) y pos 3 (cuarto)
    #poner param para un query
    pprint_response(resp)

    print("Create new sensor (POST):")
    wait_enter()
    new_sensor = { # deifnir un diccionario de un nuevo objeto, no lo pone en orden, xq no es necesario
        'name': "monitor",
        'description': "LED 4K monitor",
        'price': 1500,
    }
    resp = requests.post(f"{url}/sensors/", json=new_sensor)# va a guardar nuevo objeto, poner json
    pprint_response(resp)# resp es lo que uno envio en json

    #print("Get created sensor (GET with path param):")
    #wait_enter()
    #resp = requests.get(f"{url}/sensors/monitor")#pide path particular
    #pprint_response(resp)

    print("Get current sensors again:")
    wait_enter()
    resp = requests.get(f"{url}/sensors/")
    pprint_response(resp)

    print("Destroy created sensor (DELETE with path param):")
    wait_enter()
    resp = requests.delete(f"{url}/sensors/{sensor_name}")# poner path de archivo que quiero borrar
    # me retorna nada, por eso imprime un None tras borrarlo
    pprint_response(resp)

    print("Try to get deleted sensor again:")
    wait_enter()
    resp = requests.get(f"{url}/sensors/{sensor_name}")# el códido se cae ya que ese path no existe
    pprint_response(resp)

    print("Modify sensor:")
    wait_enter()
    resp = requests.patch(f"{url}/sensors/")# el códido se cae ya que ese path no existe
    pprint_response(resp)

    print("Send command:")
    wait_enter()
    resp = requests.put(f"{url}/sensors/{sensor_name}")# el códido se cae ya que ese path no existe
    pprint_response(resp)


if __name__ == "__main__":
    main()