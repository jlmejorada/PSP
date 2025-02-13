import random
import time
from multiprocessing.synchronize import Condition
from threading import Thread


# class Lista (Thread):
#     lista = [False, False, False, False, False]
#
#     def __init__(self, nombre):
#         Thread.__init__(self, name=nombre)
#
#     def run(self):
#         num = random.randint(0,4)
#
#         Lista.cond.acquiere()
#         while Lista.lista[num]:
#             print("El hilo", self.name, "está esperando a que se libere la posición", num)
#             Lista.cond.wait()
#
#         Lista.lista[num] = True
#         Lista.cond.release()
#
#         print("El hilo", self.name, "está usando el objeto", num)
#         time.sleep(random.randint(2,10))
#         print("El hilo", self.name, "ha terminado de usar el objeto", num)
#
#         Lista.cond.acquiere()
#         Lista.lista[num] = False
#         Lista.cond.notifyAll()
#
#         Lista.cond.release()


class Lista (Thread):
    lista = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        num = random.randint(0,4)

        with Lista.cond:
            while Lista.lista[num]:
                print("El hilo", self.name, "está esperando a que se libere la posición", num)
                Lista.cond.wait()

            Lista.lista[num] = True


        print("El hilo", self.name, "está usando el objeto", num)
        time.sleep(random.randint(1,10))
        print("El hilo", self.name, "ha terminado de usar el objeto", num)

        with Lista.cond:
            Lista.lista[num] = False
            Lista.cond.notifyAll()
