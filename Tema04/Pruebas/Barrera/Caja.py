import random
import time
from threading import *


class Caja(Thread):
    def __init__(self, nombre, barrera: Barrier) :
        Thread.__init__(self, name=nombre)
        self.barrera = barrera

    def run (self):
        print("Hilo",self.name, "entra en caja")
        time.sleep(random.randint(1,3))
        print("Hilo", self.name, "sale de caja")


if __name__ == "__main__":
    barrera = Barrier(5)
    hilos = []

    for i in range(10) :
        hilo = Caja(str(i), barrera)
        time.sleep(random.randint(1,3))
        hilo.start()
        hilos.append(hilo)

    for h in hilos:
        h.join()