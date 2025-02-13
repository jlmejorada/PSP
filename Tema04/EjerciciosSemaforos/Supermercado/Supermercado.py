import threading
import time



def atender_cliente():
    for i in range(5):
        print(f"Atendiento al cliente {i + 1}")
        time.sleep(1)
    print("Camarero: Terminó de servir todos los cafés")

if __name__ == "__main__":
    numClientes=25
    numCajas=5
    for i in range():
        hilo_caja = threading.Thread(target=atender_cliente)
        hilo_caja.start()
        hilo_caja.join()
