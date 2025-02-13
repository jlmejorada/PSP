import random
import time
from threading import *


class Trabajadores(Thread):
    bloqueo = Lock()
    trabajador = 5

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Soy { self.name } y voy a trabajar")
        Estacionamiento.semaforo.acquire()
        Estacionamiento.estacionamiento -= 1

        time.sleep(random.randint(1,10))

        print(f"\U0001F699 {self.name} salió del estacionamiento.")
        Estacionamiento.semaforo.release()
        Estacionamiento.estacionamiento += 1





if __name__ == '__main__':


    for hilo in range(5):
         trabajador = Trabajadores(f"Trabajador {hilo+1}")
         trabajador.start()

