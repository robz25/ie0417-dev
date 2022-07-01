*************
Proyecto Final
*************

Integrantes
=======
 - Katharina Alfaro Solís **B80251**
 - Robin Gonzalez **B43011**
 - German Ureña Araya **B77809**


Documentación:
==================

Requerimientos funcionales y no funcionales 
============

Requerimientos funcionales del eie-device
--------------------------
 - ``REQ-001``  Para la implementación de la biblioteca eie-device se utilizará un proyecto de Cmake, el Cmake construirá una biblioteca dinámica llamada eie-device.

 - ``REQ-002`` La biblioteca eie-device se comunicará con Mosquito empleando el cliente Paho MQTT C.

 - ``REQ-003`` Para facilitar la integración de los dispositivos con el sistema, eieDevice debe implementar una biblioteca en C, la cual debe abstraer los detalles de ditto protocol y del cliente MQTT.

 - ``REQ-004``  La biblioteca eie-device soporta el envio y recepción de mensajes a Ditto mediante MQTT para leer y actualizar el dispositivo según corresponda.     

- ``REQ-005``   La biblioteca eie-device implementa un microservicio llamado Device Discovery que notifica la creación de un nuevo dispositivo con un identificador único para ser registrado en Ditto.

 Requerimientos funcionales del eie-manager-config
--------------------------
 
 - ``REQ-006`` Debe implementarse un microservicio en python para facilitar la configuración y el despliegue del sistema (su mantenibilidad). Por lo que debe configurar políticas, las conexiones MQTT y los dispositivos en Ditto.

 - ``REQ-007`` El microservicio eie-manager-config obtiene de un archivo Json, las políticas de acceso entre dispositivos y el broker MQTT y luego las registra en el microservicio Ditto.

 - ``REQ-008`` El microservicio eie-manager-config implementa un handshake para comunicarse con la biblioteca eie-device mediante MQTT.

