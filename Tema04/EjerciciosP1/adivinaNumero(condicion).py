import random
import time
from threading import Thread, Condition

class AdivinaNumero(Thread):
    numero_secreto = random.randint(0, 100)  # Número a adivinar
    condicion = Condition()
    encontrado = False  # Indica si alguien acertó

    def __init__(self, nombre):
        super().__init__(name=nombre)

    def run(self):
        global encontrado

        while not AdivinaNumero.encontrado:
            intento = random.randint(0, 100)  # Jugador elige un número al azar

            with AdivinaNumero.condicion:
                if AdivinaNumero.encontrado:
                    break  # Si alguien ya acertó, salimos

                print(f"🎲 {self.name} intenta con el número {intento}")

                if intento == AdivinaNumero.numero_secreto:
                    print(f"🎉 {self.name} ha adivinado el número {intento}!")
                    AdivinaNumero.encontrado = True
                    AdivinaNumero.condicion.notify_all()  # Notificar a los demás hilos
                else:
                    print(f"❌ {self.name} ha fallado")
                    time.sleep(0.5)  # Simula el tiempo entre intentos

if __name__ == "__main__":
    jugadores = [AdivinaNumero(f"Jugador-{i+1}") for i in range(5)]

    for jugador in jugadores:
        jugador.start()

    for jugador in jugadores:
        jugador.join()

    print("🏁 El juego ha terminado.")
