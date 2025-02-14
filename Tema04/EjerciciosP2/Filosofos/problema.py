import random
import time
from threading import Thread, Condition


class Mesa:
    def __init__(self):
        self.palillosLibres = [True] * 5
        self.cond = Condition()


class Filosofo(Thread):
    def __init__(self, name, mesa):
        Thread.__init__(self)
        self.m = mesa
        self.n = name
        self.palillo1 = name
        self.palillo2 = (name + 1) % 5

    def run(self):
        while True:
            time.sleep(random.randint(1, 3))
            
            with self.m.cond:
                while not self.m.palillosLibres[self.palillo1]:
                    print(f"El filósofo {self.n} está esperando el palillo {self.palillo1}.")
                    self.m.cond.wait()

                self.m.palillosLibres[self.palillo1] = False
                print(f"El filósofo {self.n} ha tomado el palillo {self.palillo1}.")

            time.sleep(random.uniform(0.5, 1.5))

            with self.m.cond:
                while not self.m.palillosLibres[self.palillo2]:
                    print(f"El filósofo {self.n} está esperando el palillo {self.palillo2}.")
                    self.m.cond.wait()

                self.m.palillosLibres[self.palillo2] = False
                print(f"El filósofo {self.n} ha tomado el palillo {self.palillo2} y está comiendo.")

            time.sleep(random.randint(3, 5))

            with self.m.cond:
                self.m.palillosLibres[self.palillo1] = True
                self.m.palillosLibres[self.palillo2] = True
                print(
                    f"El filósofo {self.n} ha terminado de comer y ha soltado los palillos {self.palillo1} y {self.palillo2}.")
                self.m.cond.notify_all()


if __name__ == '__main__':
    m = Mesa()
    filosofos = [Filosofo(i, m) for i in range(5)]

    for f in filosofos:
        f.start()

    for f in filosofos:
        f.join()

