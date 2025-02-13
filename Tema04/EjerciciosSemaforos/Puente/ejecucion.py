from paso import *

if __name__ == '__main__':

    for i in range(5):

        coche = PasoPuente(f"Coche {i+1}", random.randint(0,1))
        coche.start()
        coche.join()