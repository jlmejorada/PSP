from threading import *
from time import sleep

from EjercicioCondicion.EjPanaderia.Panaderia import Comprador


class Panaderia(Thread):
    cantidadIni = 7
    cantidad = cantidadIni
    lock = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.cantidad = Panaderia.cantidad

    def compraPan(self):
        if Panaderia.cantidad > 0:
            Panaderia.cantidad -= 1

class Comprador(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        Panaderia.lock.acquire()
        print(f"Comprador {self.name} comprando pan")
        Panaderia.compraPan()
        sleep(1)
        print(f"Comprador {self.name} ha comprado pan")
        Panaderia.lock.release()

if __name__ == '__main__':
    for i in range(0, 10):
        c = Comprador(i+1)
        c.start()
        c.join()
    print(f"Quedan {Panaderia.cantidad} panes")