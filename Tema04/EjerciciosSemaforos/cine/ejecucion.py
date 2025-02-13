
import time
import random

from sala import SalaCine

if __name__ == '__main__':

    for i in range(30):
        cliente = SalaCine(f"Cliente {i+1}")
        cliente.start()
        # time.sleep(random.randint(1, 3))
