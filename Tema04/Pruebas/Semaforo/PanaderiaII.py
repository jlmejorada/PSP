from threading import Thread, Semaphore
from time import sleep

class Panaderia:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cantidad = capacidad
        self.vaciar = Semaphore(1)  # Controla que un comprador compre a la vez
        self.llenar = Semaphore(0)  # Indica al vendedor cuándo reponer

    def compraPan(self):
        self.vaciar.acquire()  # Un comprador a la vez

        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Comprador compró pan. Quedan {self.cantidad} panes.")
            sleep(1)  # Simula el tiempo de compra
            self.llenar.release()  # Indica al vendedor que reponga
        else:
            print("No hay pan disponible.")

        self.vaciar.release()  # Libera para el siguiente comprador

    def reponerPan(self):
        while True:
            self.llenar.acquire()  # Espera a que alguien compre para reponer
            self.vaciar.acquire()  # Bloquea compradores mientras repone

            if self.cantidad == 0:
                self.cantidad = self.capacidad
                print(f"Vendedor repone pan. Ahora hay {self.cantidad} panes.")
                sleep(2)  # Simula el tiempo de reposición


            self.vaciar.release()  # Libera para que compren de nuevo

class Comprador(Thread):
    def __init__(self, nombre, panaderia):
        super().__init__(name=str(nombre))
        self.panaderia = panaderia

    def run(self):
        print(f"Comprador {self.name} intentando comprar pan...")
        self.panaderia.compraPan()

class Vendedor(Thread):
    def __init__(self, panaderia):
        super().__init__()
        self.panaderia = panaderia

    def run(self):
        print("Vendedor esperando para reponer pan...")
        self.panaderia.reponerPan()

if __name__ == '__main__':
    panaderia = Panaderia(capacidad=7)

    vendedor = Vendedor(panaderia)
    vendedor.daemon = True  # Corre en segundo plano
    vendedor.start()

    compradores = [Comprador(i + 1, panaderia) for i in range(10)]

    for c in compradores:
        c.start()

    for c in compradores:
        c.join()  # Esperamos que todos terminen

    print(f"Quedan {panaderia.cantidad} panes")
