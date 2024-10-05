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

Veremos el dashboard en el navegador:

![Tutorial2](images/6.png)
