
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

 ``Paso 1``: Confirmar que hay suficiente información de los requerimientos.

 ``Paso 2``: Escoger un elemento del sistema que descomponer
Un “Business goal”: Generar una API (Application Programming Interface) capaz de controlar los dispositivos de la fábrica desde Client, con la cual sea posible conectarse con los diferentes computadores de la fábrica 
Goal Refinement: El sistema debe ser capaz de generar una amplia variedad de comandos, sin implicar un cambio para el API
Quality attribute: Performance 
Quality attribute scenario:  La API debe proporcionar la comunicación entre el cliente y el eieManager y al ingresas más comandos a los dispositivos la API no debe verse afectada. 
Paso 3:
""""""""""""""""""""""

Architectural drivers
Priority: High , High 

Paso 4: 
""""""""""""""""""""""

Escoger un concepto de diseño o patrón que satisfaga el diseño arquitectónico 
Para seguir nuestra idea de diseño se utilizará un patrón estructural, el cual utiliza el concepto de herencia para componer interfaces y definir formas de componer objetos para obtener nuevas funcionalidades como en nuestro caso con los comandos. Se puede usar el patrón estructural Bridge, en este patrón hay una alteración estructural en las clases principales y de implementación e interfaz sin tener ningún efecto entre ellas. Estas dos clases pueden ser desarrolladas de manera independiente y solo se conectan utilizando una interfaz como puente. 
Paso 5: Instancias decisiones de diseño en sub-componentes y asignar responsabilidades
La API debe ser capaz de mandar la señal de encendido y apagado del sistema dada por el cliente, al eieManager y por lo tanto a los dispositivos conectados en esta. 
La API debe ser capaz de mandar una notificación de alarma cuando algún dispositivo tenga una falla en la fábrica y por lo tanto debe mostrarla al cliente.
 
Paso 6: 
""""""""""""""""""""""
Definir las interfaces de elementos instanciados 

Paso 7: 
""""""""""""""""""""""
 Verificar, afinar requerimientos  y hacer restricciones para los elementos instanciados.

Justificar y priorizar al menos dos atributos de calidad relevantes para el diseño a partir de los objetivos de negocio.
-----------------------------

Con base a los requierimientos y los objetivos del negocio se han establecido los atributis de diseño que priorizan la modificabilidad, el rendimiento y la disponibilidad del sistema. Éstos atributos son el producto de las relaciones e interacciones con los "stakeholders" y al explorar las necesidades del sistema con base a su contexto de desarrollo.

Para cada parte del sistema eieManager y eieDevice un ejemplo de iteración usando el método de diseño ADD.
-----------------------------

Como generalidad se tiene que para ambas partes del sistema se debe ejecutar los pasos correspondientes: Plan, Do and Check.

En el caso del ``eieManager`` primero en el planeamiento de establecen los atributos de calidad y las restricciones, que corresponden a la disponibilidad y escalabilidad, así como el principio de separación de responsabilidades; para el siguiente paso se tiene segmentar los elementos que son instanciados:

- ``ConfigHandler`` cuyo fin será la de incluir la lista de dispositivos soportados con su respectiva información (nombre, grupo broadcast, datos de conexión, etc).

- ``APIServer`` Encagado de estar al servicio de solicitudes del cliente.

- ``CommandRegistry`` Lleva el control de el registro de los comandos soportados y su información.

- ``DeviceManager`` Administra el ciclo de vida de los dispositivos conectados al ``eieManager``

- ``GroupManager`` Controla los dispositivos pertenecientes a grupos broadcast.

- ``CommandInvoker`` Ejecuta los comandos solicitados por el cliente.

- ``TransportClient`` Abstrae el protocolo de comunicación para interactuar con el dispositivo.

- ``DatabaseHandler`` Wrapper de una base de datos para almacenar configuración y estado.

una vez definidos los elementos dentro del bloque ``eieManager`` se procede a analizar y revisar el diseño así como la correcta integración de sus partes.

En el ciclo de implementación del método de diseño ADD para el ``eieDevice`` se tienen que los atributos principales de calidad del mismo corresponden a la interoperatividad y que permita la concurrencia, de los elementos instanciados dentro del bloque se destacan:

- ``TransportServer`` Responde a solicitudes de comandos provenientes del TransportClient.

- ``CommandManager`` Registro y ejecución de los comandos soportados por el dispositivo.

- ``Command`` Implementa la funcionalidad del comando.

establecidos los elementos dentro del bloque ``eieDevice`` se procede a analizar y revisar el diseño así como el correcto funcionamiento de sus componentes.


Patrones de diseño y su implementación en el proyecto de software
=============

¿Cómo se puede aplicar el patrón de diseño Proxy para abstraer la interacción y comunicación con los dispositivos desde ``eieManager``?
-----------------------------

Para la estructura general del proyecto y particularmente el área encargada de la comunicación entre los dispositivos (eieDevices) y el eieManager el uso del patrón de diseño Proxy resulta fundamental ya que al implementarlo facilita 
una interface entre los datos que entran y salen del manager, filtrándose y atrapandolos de manera unificada, estandarizanda y abstrayendo 
la comunicación entre ambos elementos del sistema; además se genera una capa de comunicación segura y privada con el tráfico de datos. 
Como se comentaba anteriormente la implementación de éste patrón de diseño es aplicable principalmente entre la comunicación entre el 
controlador principal ``eieManager`` y cada uno de los dispositivos ``eieDevices``, ya que la comunicación entre ellos radica en el tráfico de datos, por lo tanto el uso de Proxy para manipular los datos entre las partes es necesario para responder a la necesidad de desarrollo que establece que se pueda integrar al sistema cualquier dispositivo ya sea sensor u actuador, sin necesidad de reprogramar al manager, y es ahí donde el Proxy se encarga de ser éste acople para que se puedan procesar los datos en la siguiente etapa.

.. note::
    Se entiende que el patrón de diseño usando Proxy corresponde a la implementación de una clase que abstrae los mensajes entre dos componentes de software.

Dentro de los componentes sugeridos en la introducción, a cuáles se les puede relacionar con este patrón?


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


