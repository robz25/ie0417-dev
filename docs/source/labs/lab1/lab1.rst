*************
Laboratorio 1
*************

Explicar cómo planear el proyecto con Agile
============


Definir lista de requerimientos funcionales y no funcionales
============


Identficarlos con números
-----------------------------

Aplique la metodología de Attribute-Driven Design (ADD) para el diseño del sistema
============


Min 2 atributos
-------------------

Una iteracion en 2 partes de sistema
--------------------------------------

Explicar subsistemas con tácticas/patrones
----------------------------------------------

Patrones de diseño, explicarlos con el proyecto
============


Proxy
---------

Command
-----------

Diagramas UML
============

Diagramas de clases
-----------------------
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
  'CommandRegistry :
  @enduml

Diagramas de secuencia
--------------------------
