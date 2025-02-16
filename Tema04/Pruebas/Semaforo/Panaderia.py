from threading import Thread, Semaphore
from time import sleep


class Panaderia:
    cantidadIni = 7
    cantidad = cantidadIni
    sf = Semaphore(cantidadIni)  # Controlamos la cantidad de panes con el semáforo

    @classmethod
    def compraPan(cls):
        Panaderia.sf.acquire()  # Bloqueamos un recurso (un pan)
        if cls.cantidad > 0:
            cls.cantidad -= 1
            print(f"Panadería: Se vendió un pan. Quedan {cls.cantidad} panes.")
            sleep(1)  # Simula el tiempo de compra
            Panaderia.sf.release()  # Liberamos el recurso
            return True
        else:
            print("Panadería: No hay más pan disponible.")
            Panaderia.sf.release()  # Aunque no haya pan, liberamos el recurso para evitar deadlocks
            return False


class Comprador(Thread):

    def __init__(self, nombre):
        super().__init__(name=str(nombre))

    def run(self):
        print(f"Comprador {self.name} intentando comprar pan...")
        if Panaderia.compraPan():
            print(f"Comprador {self.name} ha comprado pan")
            sleep(2)
        else:
            print(f"Comprador {self.name} no pudo comprar pan porque ya no hay")


if __name__ == '__main__':
    compradores = []

    for i in range(10):
        c = Comprador(i + 1)
        compradores.append(c)
        c.start()

    for c in compradores:
        c.join()  # Esperamos que terminen todos los hilos

    print(f"Quedan {Panaderia.cantidad} panes")
