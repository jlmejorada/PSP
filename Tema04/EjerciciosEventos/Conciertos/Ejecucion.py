from threading import *
from Concierto import *

if __name__ == '__main__':
    evento = Event()
    evento.set()
    compradores = [Comprador("Comprador " + str(i+1), evento) for i in range(5)]

    for comprador in compradores:
        comprador.start()
    for comprador in compradores:
        comprador.join()