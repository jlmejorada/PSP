import threading

class Contador:
    def __init__(self):
        self.valor = 0
        self.lock = threading.Lock()

    def incrementar(self, total):
        with self.lock:
            if self.valor >= total:
                return
            self.valor += 1

    def obteneValor(self):
        return self.valor

def incrementarValor(contador, total):
    while contador.obteneValor() < total:
        contador.incrementar(total)

if __name__ == "__main__":
    contador = Contador()
    hilos = []
    N = 10
    total = 10000

    for i in range(N):
        hilo = threading.Thread(target=incrementarValor, args=(contador, total))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"El valor final del contador es {contador.obteneValor()}")
