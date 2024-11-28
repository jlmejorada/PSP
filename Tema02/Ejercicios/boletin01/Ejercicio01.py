from multiprocessing import *

def sumaNumeros(number):
    suma = 0
    print("n: " + str(number))
    for i in range(1, number+1):
        suma += i
        print("Suma de todos los valores hasta el " + str(number) + ": " + str(suma))



if __name__ == "__main__":
    p1 = Process(target=sumaNumeros, args=(2, ))
    p2 = Process(target=sumaNumeros, args=(4, ))
    p3 = Process(target=sumaNumeros, args=(5, ))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
