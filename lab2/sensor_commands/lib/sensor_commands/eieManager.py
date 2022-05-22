import logging
from random import choice

from . import command
from .args import parse_args
from .sensor.manager import SensorManager# importamos comandos para manipular sensores
from .sensor.analyzers import avg_thresh_analyzer as avt

# imports de server
from fastapi import FastAPI, Body #importa 2 módulos del mismo paquete
from random import randint
from typing import Optional
from pydantic import BaseModel

log = logging.getLogger(__name__)

app = FastAPI()# instanciar un FastApi llamado app

#A IMPLEMENTAR
#------------------------------------------------------------------------------------------------

"""
    create_sensor POST
    Crear y registrar un nuevo Device. El dispositivo debe tener un identificador o nombre tipo string.

    update_sensor PATCH
    Actualizar la información de un Device específico previamente registrado.

    get_sensors GET
    Obtener la información de todos los Device registrados.

    get_sensor GET
    Obtener la información de un Device específico previamente registrado.

    delete_sensor DELETE
    Eliminar un Device específico previamente registrado.

    send_command PU
    Enviar un comando de administración a un Device específico y obtener su respuesta. La información 
    requerida para ejecutar el comando debe pasarse por medio del Body del API request y no como parte del URL.
    To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
    https://fastapi.tiangolo.com/tutorial/body/

    Algunos métodos se implementarán dentrode manager.py en folder sensor, futuro deviceManager
"""
#------------------------------------------------------------------------------------------------
args = parse_args()#crear sensores

config_name = args.config
sensor_type_name = args.sensor_type
sensor_cmd_per_period, sensor_period_sec = (100, 5)
alert_cmd_per_period, alert_period_sec = (2, 1)
analyzer_avg_thresh = 10
num_read_commands = 200
    
#creamos sensorManager
sensor_mgr = SensorManager(config_name)# se crea instancia clase SensorManager, se dispara cracion de sensores
"""
@app.post("/sensors/")
@app.patch("/sensors/")
@app.get("/sensors/")
@app.get("/sensors/{sensor_name}")
@app.delete("/sensors/{sensor_name}")
@app.put("/command/{sensor_name}")
"""

sensor_name = "humidity"

#Métodos del server de eieManager
@app.post("/sensors/")
def create_sensor(sensor: Sensor)
    """
    Create a new sensor and register it

    :param sensor sensor: sensor to register.
    """ 
    #llamar aquí función que obtiene un sensor, implementarla en manager futuro deviceManager
    new_sensor = sensor_mgr.create_sensors()
    #que acabo de pasar, creo el key con el valor sensor.name y guardo el objeto sensor con nombre sensor ahí
    return new_sensor

@app.patch("/sensors/")
def update_sensor(sensor: Sensor)
    """
    Update a sensor

    :param Sensor sensor: Sensor to update
    """
    update= sensor_cmd.update_sensors()
    return update 
    
@app.get("/sensors/")# la segunda parte del path la ponemos en la variable sensor_name
def get_sensors(first: int = 0, limit: int = 20):# hay 2 parámetros por defecto, first con valor 0 y limit con valor 20, por defecto
    """
    Get a list of the current sensors.

    :param int first: First list element to get (optional).
    :param int limit: Maximum number of elements to get (optional).
    """
    temp_sensor_names = sensor_mgr.get_sensor_names()
    return temp_sensor_names

@app.get("/sensors/{sensor_name}")# la segunda parte del path la ponemos en la variable sensor_name
def get_sensor(sensor_name: str):
    """
    Get specific sensor from name.

    :param str sensor_name: Name of the sensor to get.
    """
    #llamar aquí función que borra un sensor, implementarla en manager futuro deviceManager
    print(f"read sensor: {sensor_name}")
 

@app.delete("/sensors/{sensor_name}") # la segunda parte del path la ponemos en la variable sensor_name
def delete_sensor(sensor_name: str, status_code=204):
    """
    Unregister and delete sensor.

    :param str sensor_name: Name of the sensor to delete.
    :param int status_code: Default HTTP status code to return.
    """
    #llamar aquí función que borra un sensor, implementarla en manager futuro deviceManager
    print(f"deleted sensor: {sensor_name}")


@app.put("/command/{sensor_name}")# la segunda parte del path la ponemos en la variable sensor_name
def send_command(sensor_name: str):
    #recibe la información del comando en el bodym la recibiría con json desde el client
    """
    Get specific sensor from name.

    :param str sensor_name: Name of the sensor to get.
    """
    #llamar aquí función que da un commando a un sensor y retorna resultado, implementarla en manager futuro deviceManager
    print(f"command executed for sensor: {sensor_name}") 
    return ""

def main():#vamos a poner lo que tiene que correr de fijo apenas empieza el código
#si no es necesario nada, se deja vacio
    """
    Eie Manager application main function.
    """
    #args = parse_args()#crear sensores

    #config_name = args.config
    #sensor_type_name = args.sensor_type
    #sensor_cmd_per_period, sensor_period_sec = (100, 5)
    #alert_cmd_per_period, alert_period_sec = (2, 1)
    #analyzer_avg_thresh = 10
    #num_read_commands = 200

    # Set up command runners
#    sensor_mgr = SensorManager(config_name)# se crea instancia clase SensorManager, se dispara cracion de sensores
    #de config.json
    sensor_cmd_runner = command.CommandRunner(
        cmd_per_period=sensor_cmd_per_period,
        period_sec=sensor_period_sec)
    alert_cmd_runner = command.CommandRunner(
        cmd_per_period=alert_cmd_per_period,
        period_sec=alert_period_sec)
    sensor_cmd_runner.start()
    alert_cmd_runner.start()

    # Set up sensor analyzer with "above average threshold alert" strategy
    analyzer = avt.SensorAvgThreshAnalyzer(avg_thresh=analyzer_avg_thresh)
    avt.set_alert_handle_strategy(analyzer, alert_cmd_runner)
    avt.set_above_compare_strategy(analyzer)

    # Generate read commands for temp sensors
    temp_sensor_names = sensor_mgr.get_sensor_names_per_type(sensor_type_name)
    for _ in range(num_read_commands):
        rand_sensor_name = choice(temp_sensor_names)
        read_cmd = sensor_mgr.create_sensor_read_cmd(rand_sensor_name,
                                                     analyzer)
        sensor_cmd_runner.send(read_cmd)

    # Teardown command runners
    sensor_cmd_runner.stop()
    alert_cmd_runner.stop()


if __name__ == "__main__":
    main()
