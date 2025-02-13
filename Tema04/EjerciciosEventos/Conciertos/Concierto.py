import random
import time
from threading import *

class Comprador(Thread):
    def __init__(self, nombre, event:Event):
        Thread.__init__(self)
        self.evento = event
        self.nombre = nombre

    def run(self):
        while not self.evento.is_set():
             self.evento.wait()
        self.evento.clear()
        print("El comprador", self.nombre, "entra a comprar la entrada")
        time.sleep(random.randint(1, 3))
        print("Entrada comprada por", self.nombre)
        self.evento.set()

class Empresa(set):
    def __init__(self, event:Event):
        Thread.__init__(self)
        self.evento = event

    def run(self):
        while not self.evento.is_set():
             self.evento.wait()
        self.evento.clear()
        print("Empresa vende entradas")
        time.sleep(5)
        print("Empresa ha vendido todas las entradas")
        self.evento.set()
