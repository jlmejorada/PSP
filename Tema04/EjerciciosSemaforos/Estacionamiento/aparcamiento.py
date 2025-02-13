import random
import time
from threading import Thread, Semaphore



class Estacionamiento(Thread):
    aparcamientos = 5
    semaforo = Semaphore(aparcamientos)
    estacionamiento = aparcamientos

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        Estacionamiento.estacionamiento = self.aparcamientos
        print(f"Estacionamiento disponible {Estacionamiento.estacionamiento}")
        print(f"\U0001F699 {self.name} está entrando al estacionamiento.")
        Estacionamiento.semaforo.acquire()
        Estacionamiento.estacionamiento -= 1

        time.sleep(random.randint(1,10))

        print(f"\U0001F699 {self.name} salió del estacionamiento.")
        Estacionamiento.semaforo.release()
        Estacionamiento.estacionamiento += 1

