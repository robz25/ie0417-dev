# Laboratorio 2: EieManager
## Implementación de la funcionalidad básica del API para client
__________

Se creó un paquete con la jerarquía de módulos para implementar el prototipo del API.

`
pip install -i https://test.pypi.org/simple/ eieManagerNew==0.0.1
`



### Integrantes:

* Katharina Alfaro Solís **B80251**
* Robin González Ricz **B43011**
* German Ureña Araya **B77809**
____________
En este laboratorio, se implementó por medio de la arquitectura REST, la API que genera la comunicación entre el eieManager y el cliente. El cliente debe ser capaz de crear un dispositivo, eliminarlo, obtener la información de este, actualizar, así como obtener la información de todos los dispositivos y enviar un comando a uno de ellos y recibir la respuesta.
Para implementar el prototipo del API se debe crear un paquete de la siguiente manera: 

* Primero, se debe estar dentro del contenedor dentro de la siguiente carpeta: *_/labs/lab2/eieManager_* 
* Dentro de esta carpeta se corre el siguiente comando para instalar el paquete:

    `
    $ pip install -e .
    `

* Luego en el mismo lugar en la terminal llamamos lo siguiente:

    `
    $ eieManagerTest
    `
* De esta manera ya estamos corriendo el servidor, por lo tanto está esperando el acceso del cliente, entonces se debe abrir otra terminal dentro del contenedor esta vez en la carpeta *_/labs/lab2/eieManager/lib/eieManager_* ya que aquí se encuentra el archivo del cliente que debemos correr:

    `
    $ python3 client.py
    `

De esta manera generamos la comunicación entre el cliente y el servidor que en este caso es el eieManager. 

.. uml::

  @startuml
  APIserver -> eieManager : Notifica peticición de comunicación con un eieClient.
  eieManager -> eieDevice : Envía dirección de destino
  eieDevice --> eieManager : Confirma existencia y disposición de comunicarse
  eieManager <-> eieDevice : Handshake y configuración de comunicación

  eieManager -> eieDevice : Envía paquetes de datos
  eieManager <-- eieDevice : Confirma recepción de datos y envía respuesta
  eieManager -> eieDevice : Cierra comunicación

  eieManager -> APIserver : Envía respuesta a petición original
  @enduml
