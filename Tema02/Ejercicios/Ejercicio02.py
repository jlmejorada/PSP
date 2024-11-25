from multiprocessing import *


def suma(number):
    suma = 0;
    for i in range(1, number+1):
        suma += i;
    print("Suma de todos los valores hasta el " + str(number) + ": " + str(suma))
    return suma


if __name__ == "__main__":
    res = 0
    n = int(input("Hasta que número quieres sumar?"))
    numbers = []

    for i in range(1, n+1):
        numbers.append(i)

    with Pool(processes=3) as pool:
        res = pool.map(suma, numbers)
