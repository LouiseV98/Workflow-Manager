from prefect import task, flow
from prefect.states import Failed
import requests
import responses

# Definir la tarea que consulta el estado del servidor
@task
def check_playstation_server_status():
    try:
        # Realizamos una petición GET al endpoint del estado de PlayStation
        response = requests.get("https://status.playstation.com/es-mx/")
        
        if response.status_code == 200:
            print("El servicio de PlayStation Network esta funcionando correctamente")
        else:
            print(f"PlayStation server returned status code {response.status_code}")
            # Marcar el estado como 'Failed' si no se obtiene un código 200
            return Failed(message=f"Servidor PlayStation no disponible. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        # Marcar la tarea como fallida si ocurre una excepción
        return Failed(message=f"Error en la tarea: {e}")

# Definir el flujo
@flow
def playstation_monitor():
    check_playstation_server_status()

# Ejecutar el flujo
if __name__ == "__main__":
    playstation_monitor.serve(name="playstation-monitor", interval=30)


