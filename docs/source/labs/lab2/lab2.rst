*************
Laboratorio 2
*************

Integrantes
=======
 - Katharina Alfaro Solís **B80251**
 - Robin Gonzalez **B43011**
 - German Ureña Araya **B77809**


Documentación 
==================

Descripción detallada de los endpoints REST 
------------------------------------

    Para la implementación de este laboratorio se decidió utilizar una arquitectura tipo `REST <https://www.ibm.com/cloud/learn/rest-apis>`__
    con el fin de restringir el ``HTTP API`` de manera que este sea sencillo y confiable. 
    En este caso se implementó la ``REST API`` para generar la comunicación entre el client y el eieManager en nuestro caso.
    De forma que el servicio que realiza el accceso se denomina cliente y el servicio que contiene el recurso se denomina servidor.


    Para realizar la comunicación del ``REST API`` se utiliza HTTP como fue mencionado anteriormente, mediante el uso de 
    métodos estándar de este como GET, POST, PUT, DELETE, además de estos en nuestra implementación utilizamos PATCH, de
    forma que se logre de manera adecuada la comunicación entre el cliente y el servidor (EieManager). Además el eieManager
    tiene interacción con el deviceManager de forma que este se encargue especificamente del manejo de los dispositivos conectados
    a la fábrica. 

    **Operaciones que soporta el prototipo (métodos de la HTTP API):**

    * *def* create_device(): En esta función se utiliza el método ``POST`` @app.post("/devices/"), el cual debe crear y registrar un nuevo device. Este llama la función de deviceManager para crear un nuevo device, debe recibir un divice del Json en el body y retornar el resultado de ejecición, sucess, failed ...

    * *def* update_device(): Se utiliza el método ``PATCH`` @app.patch("/devices/"), este actualiza la información de un device específico previamente registrado. LLama a la función de deviceManager que actualiza atributos de un nuevo device, debe recibir un device del Json o ID del device y adicionalmente el diccionario de atributos a cambiar

    * *def* get_devices(): Se utiliza el método ``GET`` @app.get("/devices/"), información de todos los device registrados. Llama a la función de deviceManager que retorne todos los devices, en json, no recibe nada.

    * *def* get_device(): Se utiliza el método ``GET`` @app.get("/devices/{device_name}"), obtiene la informacion de un device específico registrado. Llama la función de deviceManager que retorne un device, en json, debe recibir el ID del device.

    * *def* delete_device(): Se utiliza el método ``DELETE`` @app.delete("/devices/{device_name}"), elimina un device específico previamente registrado. Llama la función de deviceManager que borre un device existente, debe recibir el ID del device y retornar un estado de ejecución: success, failed, no such device...

    * *def* send_command (): Se utiliza el método ``PUT`` @app.put("/devices/{device_name}"), envia un comando de administración a un device y obtiene su respuesta. Llama la función de deviceManager que envíe un comando a un device, debe recibir el ID del device y el comando en el body, o toda la información en el body, tanto ID del device como el comando.


Particularidades del diseño
------------------------------------

Nuestro diseño tiene la particularidad de que gracias a las funciones implementadas en el deviceManager que permiten modificar el .json con los devices se 
logra mejorar la mantenibilidad y escalabilidad del código, ya que se pueden modificar los devices de acuerdo a lo 
deseado por el cliente.

El servidor de nuestro diseño es el eieManager (eieManager.py), el cual se comunica con el client.py el cual solicita el acceso a los devices. Por otro lado, cuando esta comunicación sucede por medio de la 
API, el eieManager se comunica con el deviceManager el cual contiene las funciones que se aplican sobre los devices de acuerdo a lo solicitado por el client.



Si el cliente envía un comando a un dispositivo específico, se realiza el siguiente diagrama de secuencia como el siguiente:

Asumimos que el API registró la petición de comunicarse con un eieDevice

.. uml::

  @startuml
  Client -> eieManager : Notifica peticición de comunicación con un eieClient(REST API).
  eieManager -> eieDevice : Envía dirección de destino
  eieDevice --> eieManager : Confirma existencia y disposición de comunicarse
  eieManager <-> eieDevice : Handshake y configuración de comunicación

  eieManager -> eieDevice : Envía paquetes de datos
  eieManager <-- eieDevice : Confirma recepción de datos y envía respuesta
  eieManager -> eieDevice : Cierra comunicación

  eieManager -> Client : Envía respuesta a petición original(REST API).
  @enduml