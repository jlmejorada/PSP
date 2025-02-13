from cosa2 import MiThread


print("Soy el hilo principal")

for i in range(0, 10):
    t = MiThread(i)
    t.start()