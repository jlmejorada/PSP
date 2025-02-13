from threading import Thread

from EjercicioCondicion.EjPanaderia.Panaderia import *

if __name__ == '__main__':

    p = Panaderia()
    compradores = [Comprador(f"Comprador {i+1}", p) for i in range(10)]
    reponedor = Reponedor(p)

    for c in compradores:
        c.start()
    reponedor.start()

    for c in compradores:
        c.join()
    reponedor.join()


