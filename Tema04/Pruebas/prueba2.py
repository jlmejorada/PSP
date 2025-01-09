import time
import threading


def descargar_archivo(nombre, tiempo):
    print(f"Iniciando descarga de {nombre}")
    time.sleep(tiempo)  # Simula tiempo de descarga
    print(f"Descarga de {nombre} completada")

if __name__ == "__main__":
    tiempo = time.time()
    hilos = [
        threading.Thread(target=descargar_archivo, args=("Archivo 1", 3)),
        threading.Thread(target=descargar_archivo, args=("Archivo 2", 5)),
        threading.Thread(target=descargar_archivo, args=("Archivo 3", 2)),
    ]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    tiempo=time.time()-tiempo
    print(f"Todas las descargas finalizadas en {tiempo} segundos")
