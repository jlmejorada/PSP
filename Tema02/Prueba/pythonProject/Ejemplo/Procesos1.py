from multiprocessing import Process, Queue
from random import random, randint
from time import sleep

def producer(q):
    for i in range(10):
        q.put(i)
        print(i,'Enviado')
        sleep(randint(1,5))
    q.put(None)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item,'Recibido')
        sleep(randint(1,5))

if __name__ == '__main__':
    queue = Queue(maxsize=3)
    proceso1 = Process(target=producer, args=(queue,))
    proceso2 = Process(target=consumer, args=(queue,))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    print('Proceso 1 terminado')
    proceso2.join()
    print('Proceso 2 terminado')