"""
Basic REST API server using FastAPI.
"""

from fastapi import FastAPI, Body
from random import randint
from typing import Optional
from pydantic import BaseModel
from ..args import parse_args
from ..DevManager import DevMan 


class Device(BaseModel):
    identifier: str
    tipo: str           # type is a reserved word 
    commands : List[str]
    IP : str

class Commands(BaseModel):
    device_identifier: str 
    command: str
    arguments : Optional[List[str]] = None 

app = FastAPI()

arguments = parse_args()

device_manager = DevMan()
device_manager.init_devman(arguments.config)

@app.post("/devices/")
def create_device(device: Device):
    """
    Create a new device and register it

    :param Device device: Device to register.
    """
    device_resp = device_manager.create_device(
        device.identifier,
        device.tipo,
        device.commands,
        device.IP
    )
    return device_resp


@app.get("/command/")
def get_command(command: Command):
    """
    Get a command of the current info.
    """

    command_resp = device_manager.get_command(
        command.device_identifier,
        command.cmd,
        command.arguments
    )
    return command_resp


@app.delete("/devices/{device_name}")
def delete_device(device_name: str, status_code=204):
    """
    Unregister and delete item.

    :param str item_name: Name of the item to delete.
    :param int status_code: Default HTTP status code to return.
    """
    resp = device_manager.delete_device(device_name)
    return resp


@app.put("/devices/{device_name}")
def update_device(device: Device):
    """
    Update a device
    """

    resp = device_manager.update_device(
        device.identifier, 
        device.tipo, 
        device.commands, 
        device.IP
    )
    return resp


@app.put("/devices/{device_name}")
def read_device(device_name: str):
    """
    Get specific device from name.

    :param str item_name: Name of the item to get.
    """
    information = device_manager.device_info(device_name)
    return information

@app.get("/devices/")
def info_devices():
    """
    Get information of all devices
    """
    information = device_info()
    return information