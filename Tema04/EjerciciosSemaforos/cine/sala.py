import time
import random
from threading import *


class SalaCine(Thread):
    asientos = 20
    semaforo = Semaphore(asientos)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        SalaCine.asientos = self.asientos
        print(f"Asientos disponibles {SalaCine.asientos}")
        print(f" {self.name} está entrando a la sala.")
        SalaCine.semaforo.acquire()
        SalaCine.asientos -= 1

        time.sleep(random.randint(3,6))

        print(f" {self.name} salió de la sala.")
        SalaCine.semaforo.release()
        SalaCine.asientos += 1

