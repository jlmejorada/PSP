import time
from random import random
from threading import *
from time import sleep


class Panaderia (Thread):

    def __init__(self):
        Thread.__init__(self)
        self.CAPACIDAD = 7
        self.barras = self.CAPACIDAD
        self.cond = Condition()


class Comprador(Thread):
    def __init__(self, name, Panaderia):
        Thread.__init__(self)
        self.p = Panaderia
        self.n = name

    def run(self):
        with self.p.cond:
            while self.p.barras == 0:
                print(f"El comprador {self.n} está esperando a que haya pan.")
                self.p.cond.wait()

            print(f"El comprador {self.n} ha comprado una barra de pan. Quedan {self.p.barras} barras.")
            self.p.barras -= 1
            sleep(1)
            self.p.cond.notify_all()

class Reponedor(Thread):
    def __init__(self, Panaderia):
        Thread.__init__(self)
        self.p = Panaderia

    def run(self):
        while True:
            with self.p.cond:
                while self.p.barras > 0:
                    self.p.cond.wait()


                print("El reponedor está reponiendo pan.")
                sleep(3)
                self.p.barras = self.p.CAPACIDAD
                print(f"El reponedor ha repuesto pan. Ahora hay {self.p.barras} barras.")
                self.p.cond.notify_all()

