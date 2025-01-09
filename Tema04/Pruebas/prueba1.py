import threading
import time


def imprimirMensaje(mensaje):
    for _ in range(5):
        print(mensaje)
        time.sleep(0.1)

if __name__ == '__main__':
    hilo1 = threading.Thread(target=imprimirMensaje, args=("Marco",))
    hilo2 = threading.Thread(target=imprimirMensaje, args=("Polo",))
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()
    print("Finalizado")