import random
import time
from threading import *

class Hilo(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        print(f"Soy {self.nombre} y estoy trabajando")
        time.sleep(random.randint(1, 10))
        print(f"Soy {self.nombre} y he terminado de trabajar")

if __name__ == '__main__':

    for i in range(5):
        h = Hilo(i+1)
        h.start()

    for i in range(5):
        h.join()