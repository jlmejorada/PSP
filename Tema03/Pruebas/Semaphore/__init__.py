from Semaphore.supermercado import Supermercado

print("Soy el hilo principal")

for i in range(0, 10):
    t = Supermercado(i)
    t.start()