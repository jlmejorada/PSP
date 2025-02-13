from EjercicioCondicion.EjLibros.Biblioteca import *

if __name__ == '__main__':

    b = Biblioteca()
    colegas = [Estudiante(f"Estudiante {i+1}", b) for i in range(8)]

    for c in colegas:
        c.start()

    for c in colegas:
        c.join()