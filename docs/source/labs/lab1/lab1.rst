*************
Laboratorio 1
*************

Integrantes
=======

 - Katharina Alfaro Solís **B80251**
 - Robin Gonzalez **B43011**
 - German Ureña Araya **B77809**
=======


Planeamiento
==================


¿Cómo planear el proyecto con Agile?
------------------------------------

Para implementar la metodología Agile se hará uso de la estrategia srum, por lo que primero se debe definir
el equipo de trabajo del scrum, en donde el scrum máster o líder del equipo sería el arquitecto y desarrollador
principal del start-up eieLabs. Luego, el propietario del producto sería la fábrica que está contratando el desarrollo 
y el equipo de scrum en general los que van a trabajar en la creación del software. 

De manera que, para este proyecto, se puede planear como release principal para habilitar lo más rápido el
desarrollo del App, la implementación del framework del eieDevice además de definir la interfaz de la API que
permitirá la comunicación de client con eieManager, la cual es de mucha relevancia, ya que será la 
vía de comunicación con el cliente y los dispositivos de la fábrica.   

 
Requerimientos funcionales y no funcionales 
============

Requerimientos funcionales 
--------------------------
 - ``REQ-001`` El sistema deberá utilizar una API para controlar los dispositivos de la fábrica desde client, 
 con la cual es posible conectar con los diferentes computadores conectados a la fábrica. 

 - ``REQ-002`` Como usuario (client), la app deberá mostrar siempre todos los dispositivos conectados a la fábrica y
 debe ser posible tener accesso a los comandos de control y status de estos.

 - ``REQ-003`` El sistema deberá utilizar un protocolo de comunicación específico entre eieManager y las instancias 
 de eieDevice que corresponden a los dispositivos conectados en la fábrica basado en remote procedure calls (RPCs).

 - ``REQ-004`` El sistema de eieManager debe recibir las respuestas de los distintos dispositivos al enviar comandos
 a un grupo de broadcast para formar la respuesta final que se entrega al usuario. 
 
Requerimientos no funcionales 
-----------------------------
 - ``REQ-005`` El sistema debe ser capaz de generar una amplia variedad de comandos, se pueden agregar nuevos comandos
 y no deben implicar cambio para el API. 

 - ``REQ-006`` La comunicación para comandos entre eieManager y eieDevice debe estar bajo un protocolo inicial basado 
 en remote procedure calls(RPCs).

 - ``REQ-007`` Para la implementación del sistema se usará el lenguaje de programación Python. 

Aplique la metodología Attribute-Driven Design (ADD) para el diseño del sistema
============

Patrones de diseño, explicarlos con el proyecto
=============

Diagramas UML
=============

Diagramas de clases
-----------------------

Diagrama de clases para el programa eieManager.

.. uml::

  @startuml
  'definir clases
  class ConfigHandler
  class APIServer
  Abstract CommandRegistry
  class CommandInfo
  abstract DeviceManager
  abstract GroupManager
  class Group
  class CommandInvoker
  class TransportClient
  class DatabaseHandler
  class RPCClient
  class Device


  'Definir relacion entre clases
  'realization CommandRegistry es clase abstracta, interfaz de CommandInfo
  'realization
  GroupManager <|.. Group
  CommandRegistry <|.. CommandInfo
  'Asociación, no queremos que CommandRegistry accese a CommandInvoker
  CommandRegistry --> CommandInvoker
  'Asociación
  TransportClient --> RPCClient
  DeviceManager --> Device
  APIServer --> TransportClient
  DeviceManager -- GroupManager
  'Composición, los grupos se forman totalmente de dispositivos
  Group *-- Device
  'Dependencia
  ConfigHandler ..> DatabaseHandler



  'Definir métodos y atributos
  CommandRegistry : addCommand()
  CommandRegistry : deleteCommand()
  CommandRegistry : modifyCommand(field, data)
  GroupManager : createGroup()
  GroupManager : deleteGroup()
  GroupManager : editGroup()
  GroupManager : editGroupMembers()
  TransportClient : newConnection()
  TransportClient : closeConnection()
  TransportClient : readData()
  TransportClient : sendData()
  TransportClient : standby()
  APIServer : processRequest()
  DeviceManager : addDevice()
  DeviceManager : removeDevice()
  DeviceManager : editDevice()
  DeviceManager : listDevice()
  DeviceManager : broadCastMessage()
  DeviceManager : sendMessage()
  ConfigHandler : storeConfig()
  ConfigHandler : readConfig()
  RPCClient : send()

  @enduml

Diagrama de clases para el programa eieDevice.

.. uml::

  @startuml
  'definir clases
  class TransportServer
  abstract CommandManager
  class Command

  'Definir relacion entre clases
  'realización, CommandManager es interfaz para command
  CommandManager <|-- Command
  'Dependencia, TransportServer utiliza CommandManager
  TransportServer <.. CommandManager

  'Definir métodos y atributos
  CommandManager : parseCommand()
  CommandManager : buildCommand()
  TransportServer : recieveData()
  TransportServer : sendData()
  TransportServer : standby()
  @enduml

Diagramas de secuencia
--------------------------

Caso 1 El cliente envía un comando a un dispositivo específico. 

Asumimos que el API registró la petición de comunicarse con un eieDevice

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

Caso 2 El cliente envía un comando a un grupo de broadcast.

.. uml::

  @startuml
  eieManager -> eieDevice : Espera canal libre y envía dirección genérica de broadcast
  eieDevice --> eieManager : Mantiene canal libre para comunicación
  eieManager <-> eieDevice : Envía configuración de comunicación

  eieDevice --> eieManager : Mantiene canal libre para comunicación
  eieManager --> eieDevice : Envía paquetes de datos
  eieDevice --> eieManager : Mantiene canal libre para comunicación
  eieManager -> eieDevice : Cierra comunicación
  @enduml

