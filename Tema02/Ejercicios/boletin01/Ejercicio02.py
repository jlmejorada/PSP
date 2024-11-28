from multiprocessing import *


def sumaNumeros(id, number):
    suma = 0;
    print("Proceso " + str(id))
    for i in range(1, number+1):
        suma += i;
        print("Suma de todos los valores hasta el " + str(number) + ": " + str(suma))
    return suma


if __name__ == "__main__":
    with Pool(processes=3) as pool:
        numbers=[(1,2), (2,4), (3,5), (4,7), (5,8)]

        resultados = pool.starmap(sumaNumeros, numbers)

    print("Resultados:", resultados)