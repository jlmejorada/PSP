import time
import random
from threading import Thread, Event, Lock


class Empresa(Thread):
    def __init__(self, evento: Event):
        super().__init__()
        self.evento = evento
        self.entrada_actual = 1
        self.lock = Lock()

    def run(self):
        print("📢 La empresa ha iniciado la venta de entradas.")
        self.evento.set()  # Permite comprar
        time.sleep(5)  # Simula 5 horas de venta
        self.evento.clear()  # Cierra la venta
        print("⛔ La empresa ha cerrado la venta.")

    def vender_entrada(self):
        with self.lock:
            if self.evento.is_set():
                ticket = self.entrada_actual
                self.entrada_actual += 1
                return ticket
            return None  # Venta cerrada


class Comprador(Thread):
    def __init__(self, nombre, empresa: Empresa, evento: Event):
        super().__init__(name=str(nombre))
        self.empresa = empresa
        self.evento = evento

    def run(self):
        self.evento.wait()  # Espera a que la empresa abra la venta
        ticket = self.empresa.vender_entrada()

        if ticket:
            print(f"✅ Comprador {self.name} compró la entrada {ticket}.")
            time.sleep(random.uniform(0.5, 1.5))  # Simula tiempo de compra
        else:
            print(f"❌ Comprador {self.name} no pudo comprar, venta cerrada.")


if __name__ == '__main__':
    evento = Event()
    empresa = Empresa(evento)
    empresa.start()

    compradores = [Comprador(i + 1, empresa, evento) for i in range(30)]

    for c in compradores:
        c.start()
        time.sleep(0.2)

    empresa.join()  # Espera a que la empresa termine

    for c in compradores:
        c.join()  # Espera a que todos los compradores terminen

    print("🎟️ Fin del programa.")
