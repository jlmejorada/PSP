from threading import *

class Hilo(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        print(f"Soy el hilo {self.num}")

if __name__ == '__main__':
    print("Soy el hilo principal")

    for i in range(10):
        h = Hilo(i)
        h.start()

    for i in range(10):
        h.join()