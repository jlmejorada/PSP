import random
import time
from threading import Thread, Condition

class Lista(Thread):
    lista = [False] * 5  # 5 recursos compartidos
    cond = Condition()

    def __init__(self, nombre):
        super().__init__(name=str(nombre))  # Nombre en string para evitar errores

    def run(self):
        num = random.randint(0, 4)  # Seleccionar una posición aleatoria

        with Lista.cond:
            while Lista.lista[num]:  # Espera si el recurso está ocupado
                print(f"El hilo {self.name} está esperando a que se libere la posición {num}")
                Lista.cond.wait()  # Espera hasta que alguien libere el recurso

            Lista.lista[num] = True  # Marca el recurso como ocupado

        print(f"El hilo {self.name} está usando el objeto {num}")
        time.sleep(random.randint(1, 5))  # Simula uso del recurso
        print(f"El hilo {self.name} ha terminado de usar el objeto {num}")

        with Lista.cond:
            Lista.lista[num] = False  # Libera el recurso
            Lista.cond.notify_all()  # Notifica a todos los hilos en espera

if __name__ == '__main__':
    hilos = [Lista(i) for i in range(10)]  # Crear 10 hilos

    for h in hilos:
        h.start()  # Iniciar todos los hilos

    for h in hilos:
        h.join()  # Esperar a que todos los hilos terminen

    print("Todos los hilos han terminado.")
