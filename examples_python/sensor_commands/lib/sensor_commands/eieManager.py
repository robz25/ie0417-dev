import logging
from random import choice

from . import command
#import command
from .args import parse_args
#from args import parse_args
from .sensor.manager import SensorManager# importamos comandos para manipular devicees
#from device.manager import deviceManager# importamos comandos para manipular devicees
from .sensor.analyzers import avg_thresh_analyzer as avt
#from device.analyzers import avg_thresh_analyzer as avt

# imports de server
from fastapi import FastAPI, Body #importa 2 módulos del mismo paquete
from random import randint
from typing import Optional
from pydantic import BaseModel

log = logging.getLogger(__name__)

app = FastAPI()# instanciar un FastApi llamado app

class device(BaseModel): # qué es sBaseModel y pydantic?
    name: str
    description: Optional[str] = None #el str es opcional, en caso de no proveerse, poner un None
    #conveción en Python
    price: int

devices = {# diccionario de objetos Item, key, nombre del item : value, objeto Item
    "sensor_humedad": device(
        name="sensor_humedad",
        description="sensor de humedad",
        price=randint(1000, 10000)
    ),
}
#A IMPLEMENTAR
#------------------------------------------------------------------------------------------------

"""
    create_device POST
    Crear y registrar un nuevo Device. El dispositivo debe tener un identificador o nombre tipo string.

    update_device PATCH
    Actualizar la información de un Device específico previamente registrado.

    get_devices GET
    Obtener la información de todos los Device registrados.

    get_device GET
    Obtener la información de un Device específico previamente registrado.

    delete_device DELETE
    Eliminar un Device específico previamente registrado.

    send_command PU
    Enviar un comando de administración a un Device específico y obtener su respuesta. La información 
    requerida para ejecutar el comando debe pasarse por medio del Body del API request y no como parte del URL.
    To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
    https://fastapi.tiangolo.com/tutorial/body/

    Algunos métodos se implementarán dentrode manager.py en folder device, futuro deviceManager
"""
#------------------------------------------------------------------------------------------------
args = parse_args()#crear devicees

config_name = args.config
sensor_type_name = args.sensor_type
#device_cmd_per_period, device_period_sec = (100, 5)
#alert_cmd_per_period, alert_period_sec = (2, 1)
#analyzer_avg_thresh = 10
#num_read_commands = 200
    
#creamos deviceManager
device_mgr = SensorManager(config_name)# se crea instancia clase deviceManager, se dispara cracion de devicees
"""
@app.post("/devices/")
@app.patch("/devices/")
@app.get("/devices/")
@app.get("/devices/{device_name}")
@app.delete("/devices/{device_name}")
@app.put("/command/{device_name}")
"""

device_name = "humidity"

#Métodos del server de eieManager
@app.post("/devices/")
def create_device(device: device):
    """
    Create a new device and register it

    :param device device: device to register.
    """ 
    #llamar aquí función que crea un device, implementarla en manager futuro deviceManager
    #new_device = device_mgr.create_device() #aún no implementada
    #que acabo de pasar, creo el key con el valor device.name y guardo el objeto device con nombre device ahí
    devices[device.name] = device # en el diccionario de objetos items, guarar en la posición item.name el objeto item
    #que acabo de pasar, creo el key con el valor item.name y guardo el objeto Item con nombre item ahí
    return device

@app.patch("/devices/")
#def update_device(device: device,device_name: str):
def update_device(device: device):
    """
    usar String para identificar dispositivo y objeto device para sobreescribirlo
    Update a device

    :param device device: device to update
    """
    #update = device_mgr.update_devices()
    print(f"updated device: {device_name}")
    #return update 
    #return "holi"
    return device
    
@app.get("/devices/")# la segunda parte del path la ponemos en la variable device_name
def get_devices(first: int = 0, limit: int = 20):# hay 2 parámetros por defecto, first con valor 0 y limit con valor 20, por defecto
    """
    Get a list of the current devices.

    :param int first: First list element to get (optional).
    :param int limit: Maximum number of elements to get (optional).
    """
    temp_device_names = device_mgr.get_sensor_names()
    return temp_device_names[first : first + limit ]

@app.get("/devices/{device_name}")# la segunda parte del path la ponemos en la variable device_name
def get_device(device_name: str):
    """
    Get specific device from name.

    :param str device_name: Name of the device to get.
    """
    #llamar aquí función que muestra un device, implementarla en manager futuro deviceManager
    print(f"read device: {device_name}")
 

@app.delete("/devices/{device_name}") # la segunda parte del path la ponemos en la variable device_name
def delete_device(device_name: str, status_code=204):
    """
    Unregister and delete device.

    :param str device_name: Name of the device to delete.
    :param int status_code: Default HTTP status code to return.
    """
    #llamar aquí función que borra un device, implementarla en manager futuro deviceManager
    print(f"deleted device: {device_name}")


@app.put("/command/{device_name}")# la segunda parte del path la ponemos en la variable device_name
def send_command(device_name: str):
    #recibe la información del comando en el bodym la recibiría con json desde el client
    """
    Get specific device from name.

    :param str device_name: Name of the device to get.
    """
    #llamar aquí función que da un commando a un device y retorna resultado, implementarla en manager futuro deviceManager
    print(f"command executed for device: {device_name}") 
    return ""

"""
def main():#vamos a poner lo que tiene que correr de fijo apenas empieza el código
#si no es necesario nada, se deja vacio
   
   # Eie Manager application main function.

    #args = parse_args()#crear devicees

    #config_name = args.config
    #device_type_name = args.device_type
    #device_cmd_per_period, device_period_sec = (100, 5)
    #alert_cmd_per_period, alert_period_sec = (2, 1)
    #analyzer_avg_thresh = 10
    #num_read_commands = 200

    # Set up command runners
#    device_mgr = deviceManager(config_name)# se crea instancia clase deviceManager, se dispara cracion de devicees
    #de config.json
    device_cmd_runner = command.CommandRunner(
        cmd_per_period=device_cmd_per_period,
        period_sec=device_period_sec)
    alert_cmd_runner = command.CommandRunner(
        cmd_per_period=alert_cmd_per_period,
        period_sec=alert_period_sec)
    device_cmd_runner.start()
    alert_cmd_runner.start()

    # Set up device analyzer with "above average threshold alert" strategy
    analyzer = avt.deviceAvgThreshAnalyzer(avg_thresh=analyzer_avg_thresh)
    avt.set_alert_handle_strategy(analyzer, alert_cmd_runner)
    avt.set_above_compare_strategy(analyzer)

    # Generate read commands for temp devices
    temp_device_names = device_mgr.get_device_names_per_type(device_type_name)
    for _ in range(num_read_commands):
        rand_device_name = choice(temp_device_names)
        read_cmd = device_mgr.create_device_read_cmd(rand_device_name,
                                                     analyzer)
        device_cmd_runner.send(read_cmd)

    # Teardown command runners
    device_cmd_runner.stop()
    alert_cmd_runner.stop()


if __name__ == "__main__":
    main()

"""
