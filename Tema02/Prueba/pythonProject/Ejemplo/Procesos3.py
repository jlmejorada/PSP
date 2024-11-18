from multiprocessing import Pipe, Process
from random import randint


def bombo(pipe):
    lista = []
    while True:
        if pipe.recv()==0:
            numero = randint(1, 100)
            while numero in lista:
                numero = randint(1, 100)
            lista.append(numero)
            print("El " + str(numero))
            pipe.send(numero)
        else:
            pipe.close()
            break

def jugador(pipe):
    creditos=10
    apuesta = randint(1, 100)
    while creditos > 0:
        pipe.send(0)
        creditos -= 1
        numero = pipe.recv()
        if numero == apuesta:
            print("He ganado!!!")
            pipe.send(1)
            return
        else:
            print("Rayos y retruecanos!!")
    print("El diablo, me quitan la casa")
    pipe.close()

if __name__ == "__main__":
    pipe1,pipe2=Pipe()
    p1 = Process(target=bombo, args=(pipe1,))
    p2 = Process(target=jugador, args=(pipe2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()