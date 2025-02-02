# Workflow-Manager
 Script en Python para monitorear el estado de los servicios de PlayStation utilizando Prefect.

## Instalación Prefect
Para comenzar primero necesitamos instalar la herramienta Prefect usando pip. Se
recomienda utilizar un entorno virtual en Python:
```bash
pip install -U prefect
```
Para confirmar que Prefect fue instalado correctamente, usamos este comando:
```bash
prefect version
```
Después deberiamos poder ver algo similar a esto:

![Tutorial](images/3.png)

Una vez hecho esto, iniciaremos un servidor API local:
```bash
prefect server start
```
Nos deberá aparecer este mensaje el cual nos da un enlace directo que abrirá el dashboard del servidor en el navegador:

![Tutorial1](images/5.png)

## Prefect Server
Veremos el dashboard en el navegador:

![Tutorial2](images/6.png)

Esta herramienta contiene muchas funciones las cuales no describiré, solamente me enfocaré en lo que utilicé para crear el ejemplo.
Para fines de prueba, usé esta biblioteca en Python para simular respuestas de un servidor no disponible:
```bash
pip install responses
```
En el dashboard tenemos una opción llamada Deployments en la cual podemos monitorear todas las implementaciones que hemos hecho utilizando el servidor, en este caso creé una implementación llamada playstation-monitor la cual deberá aparecer en el dashboard.

![Tutorial3](images/8.png)

Vendría siendo la tercera en la lista.
De momento esta como "Not Ready" ya que aun no he ejecutado el script en Python para que comience a funcionar.
En esta misma función del dashboard podemos modificar las implementaciones con interfaz, podemos ajustar cada implementación como queramos.

![Tutorial4](images/9.png)

En la imagen podemos observar las pruebas que he estado haciendo, así como la opción de ajustar el intervalo de tiempo, ajustes generales, etc.

### Nota:
Si es la primera vez que creas una implementación, por lógica, la implementación no se mostrará en el dashboard hasta que ejecutes el script.


Una vez ejecutemos el script, podremos ver mensajes en la consola, así como la implementación en Deployments en el servidor del navegador.

![Tutorial5](images/12.png)

Podemos ver que la tarea ha sido completada correctamente y que hay otra programada para ejecutarse dentro de unos segundos (30).
Así podremos tener control sobre los servicios de PlayStation, ya que cada cierto tiempo el servidor estará monitoreando su estado. 
Para el caso contrario, utilizaré la biblioteca responses para simular una caída del servidor.


Podemos ver que el flujo se creó y funciona correctamente.
También lo podemos comprobar en el dashboard.

![Tutorial6](images/13.png)

Una vez ejecutado el scrip, podremos ver las pruebas en el dashboard.
Podemos ver en las impresiones de consola que algo ocurrió con el servidor y mando un error 404. Ahora lo verificamos en el navegador.

![Tutorial7](images/14.png)

Para esto debemos ir a la función Runs para verificar el estado de los flujos.

![Tutorial8](images/10.png)

Ya ha habido 5 tareas fallidas debido a que el servidor se encuentra caido, aquí las podemos visualizar.
En el panel dashboard también podemos observar las tareas totales completadas, canceladas y fallidas.

![Tutorial9](images/11.png)

Gracias a esta herramienta podemos crear, ejecutar y monitorear fácilmente tareas. 
