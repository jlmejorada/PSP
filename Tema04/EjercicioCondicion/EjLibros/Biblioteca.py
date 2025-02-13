import random
import time
from threading import Thread, Condition

class Biblioteca(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.libros_libres = [True] * 8
        self.cond = Condition()

class Estudiante(Thread):
    def __init__(self, name, biblioteca):
        Thread.__init__(self)
        self.b = biblioteca
        self.n = name
        self.libro1 = random.randint(0, 8)
        self.libro2 = random.randint(0, 8)
        while self.libro1 == self.libro2:
            self.libro2 = random.randint(0, 8)

    def run(self):
        with self.b.cond:
            while self.b.libros_libres[self.libro1] == False or self.b.libros_libres[self.libro2] == False:
                print(f"El estudiante {self.n} está esperando a que el libro {self.libro1} y el libro {self.libro2} estén libres.")
                self.b.cond.wait()

            self.b.libros_libres[self.libro1] = False
            self.b.libros_libres[self.libro2] = False

        print(f"El estudiante {self.n} ha cogido el libro {self.libro1} y el libro {self.libro2}.")
        time.sleep(random.randint(3, 5))
        print(f"El estudiante {self.n} ha devuelto el libro {self.libro1} y el libro {self.libro2}.")
        time.sleep(random.randint(2, 3))

        with self.b.cond:
            self.b.libros_libres[self.libro1] = True
            self.b.libros_libres[self.libro2] = True
            self.b.cond.notify_all()