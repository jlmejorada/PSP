import random
import time
from threading import *



class Raton(Thread):
    def __init__(self, nombre, event:Event):
        Thread.__init__(self)
        self.evento = event
        self.nombre = nombre
    def run(self):
        while not self.evento.is_set():
             self.evento.wait()

        self.evento.clear()
        print("El ratón", self.nombre, "toma el control del plato")
        time.sleep(random.randint(1, 3))
        print("El ratón", self.nombre, "termina de comer")
        self.evento.set()


if __name__ == '__main__':
    evento = Event()
    evento.set()
    ratones = [Raton("Ratón " + str(i+1), evento) for i in range(5)]

    for raton in ratones:
        raton.start()
    for raton in ratones:
        raton.join()
    print("Todos los ratones han terminado de comer")
    print("Fin del programa")