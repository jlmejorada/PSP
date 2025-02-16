import random
import time
from threading import *


class Parking(Thread):
    huecos = 5
    semaforo = Semaphore(huecos)
    espacio = huecos

    def __init__(self, coche):
        Thread.__init__(self, name=coche)

    def run(self):
        Parking.semaforo.acquire()
        print(f"El coche {self.name} ha entrado en el aparcamiento")
        Parking.espacio-=1
        time.sleep(random.randint(1,10))
        print(f"El coche {self.name} está saliendo del aparcamiento")
        Parking.semaforo.release()
        Parking.espacio+=1

if __name__ == "__main__":
    aparcamientos = []

    for i in range(10):
        s = Parking(i + 1)
        aparcamientos.append(s)
        s.start()

    for c in aparcamientos:
        c.join()