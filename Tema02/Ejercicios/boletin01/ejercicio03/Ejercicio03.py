from multiprocessing import Queue, Process


def leeFichero(cola: Queue):
    with open("fichero", "r") as fichero:
        for line in fichero.readlines():
            num = int(line)
            cola.put(num)
            print("Lee " + str(num))
        cola.put(None)

def sumaNumeros(cola: Queue):
    numero = cola.get()
    while numero is not None:
        suma = 0
        for i in range(1,numero+1):
            suma += i
        print("Suma hasta " + str(numero) + ": " + str(suma))
        numero = cola.get()
    return suma

if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=leeFichero, args=(queue,))
    p2 = Process(target=sumaNumeros, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()