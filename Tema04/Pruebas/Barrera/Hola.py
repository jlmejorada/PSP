from threading import *
import time

def function():
    print("Hola mundo")

if __name__ == "__main__":
    temporizador = Timer(5, function)
    temporizador.start()
    print("Esperando a que termine el temporizador")