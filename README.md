PROYECTO URBAN GROCERS

Este proyecto forma parte del bootcamp Triple Ten y tiene como objetivo automatizar pruebas para verificar cómo la aplicación Urban Grocers crea kits de productos. Urban Grocers es una aplicación de entrega desarrollada por el equipo de Triple Ten con propósitos académicos para sus estudiantes del bootcamp de QA Engineer. Permite a los usuarios hacer compras de productos de los almacenes registrados, crear kits con varios productos, verificar la existencia de productos en almacenes específicos y buscar kits predeterminados de productos.

Instalación
Para ejecutar las pruebas automatizadas, se realizó lo siguiente:
1. Vincular las cuentas de TripleTen y GitHub.
2. Clonar este repositorio en la máquina local:
“git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git”
3. Instalar PyCharm y dentro del mismo, instalar Python.
4. Instalar las siguientes librerías Python desde PyCharm:
   - pytest
   - requests

Ejecución de las pruebas
Para ejecutar las pruebas automatizadas, se realizó lo siguiente:
1. Acceder al servidor donde se puede consultar la API de Urban Grocers.
2. Ejecutar PyCharm y abrir el proyecto clonado.
3. Crear los siguientes archivos en el proyecto:
   - configuration.py: Almacena las rutas necesarias.
   - data.py: Contiene el cuerpo de las solicitudes POST.
   - sender_stand_request.py: Almacena todas las solicitudes necesarias para resolver la tarea.
   - create_kit_name_kit_test.py: La lista completa de comprobaciones está en este archivo.

Pruebas automatizadas
Este proyecto incluye una lista de comprobación para las pruebas automatizadas. A continuación se detallan las pruebas que se realizaron, junto con los criterios de éxito y los códigos de respuesta esperados.
1. Número permitido de caracteres (1):
   - Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud.
   - Código de respuesta esperado: 201
2. Número permitido de caracteres (511):
   - Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud.
   - Código de respuesta esperado: 201
3. Número de caracteres menor que la cantidad permitida (0):
   - Código de respuesta esperado: 400
4. Número de caracteres mayor que la cantidad permitida (512):
   - Código de respuesta esperado: 400
5. Se permiten caracteres especiales:
   - Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud.
   - Código de respuesta esperado: 201
6. Se permiten espacios:
   - Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud.
   - Código de respuesta esperado: 201
7. Se permiten números:
   - Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud.
   - Código de respuesta esperado: 201
8. El parámetro no se pasa en la solicitud:
   - Código de respuesta esperado: 400
9. Se ha pasado un tipo de parámetro diferente (número):
   - Código de respuesta esperado: 400




