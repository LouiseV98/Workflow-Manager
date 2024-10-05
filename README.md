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
De momento esta como "No Ready" ya que aun no he ejecutado el script en Python para que comience a funcionar.
En esta misma función del dashboard podemos modificar las implementaciones con interfaz, podemos ajustar cada implementación como queramos.

