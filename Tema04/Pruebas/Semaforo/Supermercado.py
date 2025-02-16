from threading import *
import random
import time

class Supermercado(Thread):
    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre

    def run(self):
        print(f"Comprador {self.name} va a una caja")
        Supermercado.semaforo.acquire()
        print(f"Comprador {self.name} está siendo atendido")
        time.sleep(random.randint(1,10))
        print(f"Comprador {self.name} está pagando")
        Supermercado.semaforo.release()
        print(f"Comprador {self.name} abandona el supermercado")

if __name__ == '__main__':
    compradores = []

    for i in range(10):
        s = Supermercado(i + 1)
        compradores.append(s)
        s.start()

    for c in compradores:
        c.join()  
