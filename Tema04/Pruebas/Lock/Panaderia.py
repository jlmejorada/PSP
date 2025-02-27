from threading import Thread, Lock
from time import sleep


class Panaderia:
    cantidadIni = 7
    cantidad = cantidadIni
    lock = Lock()

    @classmethod
    def compraPan(cls):
        with cls.lock:  # Usamos `with` para manejar el Lock de forma segura
            if cls.cantidad > 0:
                print(f"Panadería: Se vendió un pan. Quedan {cls.cantidad - 1} panes.")
                cls.cantidad -= 1
                return True
            else:
                print("Panadería: No hay más pan disponible.")
                return False


class Comprador(Thread):

    def __init__(self, nombre):
        super().__init__(name=str(nombre))  # Convertimos nombre a string para evitar problemas

    def run(self):
        print(f"Comprador {self.name} intentando comprar pan...")
        if Panaderia.compraPan():
            sleep(1)
            print(f"Comprador {self.name} ha comprado pan")
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
