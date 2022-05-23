import logging
from random import choice

from . import command
#import command
from .args import parse_args
#from args import parse_args
from .deviceManager.deviceManager import DeviceManager# importamos comandos para manipular devicees
#from device.manager import deviceManager# importamos comandos para manipular devicees
#from .sensor.analyzers import avg_thresh_analyzer as avt #not used
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

devices = {# diccionario de objetos Item, key, nombre del item : value, objeto Item, para pruebas
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

    send_command PUT
    Enviar un comando de administración a un Device específico y obtener su respuesta. La información 
    requerida para ejecutar el comando debe pasarse por medio del Body del API request y no como parte del URL.
    To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
    https://fastapi.tiangolo.com/tutorial/body/

    Métodos se implementarán dentrode manager.py en folder device, futuro deviceManager
"""
#------------------------------------------------------------------------------------------------
args = parse_args()#crear devicees

config_name = args.config
device_type_name = args.device_type
#device_cmd_per_period, device_period_sec = (100, 5)
#alert_cmd_per_period, alert_period_sec = (2, 1)
#analyzer_avg_thresh = 10
#num_read_commands = 200
    
#creamos deviceManager
device_mgr = DeviceManager(config_name)# se crea instancia clase deviceManager, se dispara cracion de devicees
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
    
    """
    Todo: Llamar función de deviceManager que cree un nuevo device, debe recibir debice en Json, el device, en el body, y
    retornar el resultado de ejecución, sucess, failed...
    """
    print(device_mgr.create_device("device01", "Sensor",["X","Y"], "8080"))

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
    """
    Todo: Llamar función de deviceManager que actualice atributos de un nuevo device, debe recibir o device en Json,
    o ID del device y adicionalmente el diccionario de atributos a cambiar, tal vez es más fácil lo primero
    """
    device_mgr.update_device("Device-02")
    print(f"updated device: {device_name}")    
    return device
    
@app.get("/devices/")# la segunda parte del path la ponemos en la variable device_name
def get_devices(first: int = 0, limit: int = 20):# hay 2 parámetros por defecto, first con valor 0 y limit con valor 20, por defecto
    """
    Get a list of the current devices.

    :param int first: First list element to get (optional).
    :param int limit: Maximum number of elements to get (optional).
    """
    """
    Todo: Llamar función de deviceManager que retorne todos los devices existentes, en json(texto), no recibe nada
    """
    temp_device_names = device_mgr.get_device_names()
    return temp_device_names[first : first + limit ]

@app.get("/devices/{device_name}")# la segunda parte del path la ponemos en la variable device_name
def get_device(device_name: str):
    """
    Get specific device from name.

    :param str device_name: Name of the device to get.
    """
    """
    Todo: Llamar función de deviceManager que retorne un device, en json, deberi recibir el ID del device
    """
    device_info = device_mgr.get_device("Device-03")
    print(device_info)

    #llamar aquí función que muestra un device, implementarla en manager futuro deviceManager
    print(f"read device: {device_name}")
 

@app.delete("/devices/{device_name}") # la segunda parte del path la ponemos en la variable device_name
def delete_device(device_name: str, status_code=204):
    """
    Unregister and delete device.

    :param str device_name: Name of the device to delete.
    :param int status_code: Default HTTP status code to return.
    """
    """
    Todo: Llamar función de deviceManager que borre un device existente, debe recibir el ID del device y retornar un estado
    de ejecución ejemplo: success, failed, no such device...
    """
    print(device_mgr.delete_device("Device-04"))
    
    print(f"deleted device: {device_name}")


@app.put("/command/{device_name}")# la segunda parte del path la ponemos en la variable device_name
def send_command(device_name: str):
    """
    Get specific device from name.

    :param str device_name: Name of the device to get.
    """
    """
    Todo: Llamar función de deviceManager que envíe un comando a un device, debe recibir el ID del device y el comando 
    en el body, tanto ID del device como Comando, el body es formato json
    """
    #llamar aquí función que da un commando a un device y retorna resultado, implementarla en manager futuro deviceManager
    print(f"command executed for device: {device_name}") 
    return ""
