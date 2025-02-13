import random
import time

from EjerciciosSemaforos.Estacionamiento.aparcamiento import Estacionamiento

if __name__ == '__main__':
    numAutos =10
    vehiculos = []

    for index in range(numAutos):

        vehiculo = Estacionamiento(f"Vehiculo {index+1}")
        vehiculos.append(vehiculo)
        vehiculo.start()

    for vehiculo in vehiculos:
        vehiculo.join()