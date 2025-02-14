import random
from threading import *

class Bloquea(Thread):
    lista = [False] *5
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Hilo {self.name} ejecutandose")

        pos = random.randint(0, 4)
        print(f"Hilo {self.name} quiere tomar la posición {pos}")

        Bloquea.bloqueo.acquire()
        if not Bloquea.lista[pos]:
            Bloquea.lista[pos] = True
            print(f"Hilo {self.name} ha tomado la posición {pos}")
        Bloquea.bloqueo.release()

if __name__=='__main__':

    for i in range(0,5):
        h = Bloquea(i)
        h.start()

    for i in range(0,5):
        h.join()