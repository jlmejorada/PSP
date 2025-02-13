import random
from threading import *


class AdivinaNumero():
    numero = random.randint(0, 100)
    avisar = False
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.name = nombre

    def run(self):
        num = random.randint(0, 100)

        with AdivinaNumero.cond:
            while AdivinaNumero.avisar:
                print("El jugador", self.name, "ha fallado")
                Lista.cond.wait()

            Lista.lista[num] = True

        print("El hilo", self.name, "está usando el objeto", num)
        time.sleep(random.randint(1, 10))
        print("El hilo", self.name, "ha terminado de usar el objeto", num)

        with Lista.cond:
            Lista.lista[num] = False
            Lista.cond.notifyAll()