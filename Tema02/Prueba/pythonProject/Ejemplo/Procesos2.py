from multiprocessing import Process, Queue
from random import randint
from time import sleep

def procducer(q, id):
    for i in range(10):
        if q.full():
            print(f"P{id}: la cola está llena")
        q.put(i)
        print(f"P{id}: He puesto", i)
        sleep(randint(1, 5))
    q.put(None)
    print(f"P{id}: ha acabado")

def consumer(q, id):
    while True:
        if q.empty():
            print(f"C{id}: No hay nada en la cola")
        item = q.get()
        if item is None:
            break
        print(f"C{id}: He recibido", item)
        sleep(randint(1, 5))
    print(f"C{id}: No hay más elementos en la cola")

if __name__ == '__main__':
    productores = []
    consumidores = []
    queue = Queue(maxsize=3)
    for i in range(3):
        productores.append(Process(target=procducer, args=[queue,i, ]))
    for i in range(2):
        consumidores.append(Process(target=consumer, args=[queue,i, ]))
    for i in range(3):
        productores[i].start()
    for i in range(2):
        consumidores[i].start()
    for i in range(3):
        productores[i].join()
    for i in range(2):
        consumidores[i].join()
    print("Todas las tareas han acabado")