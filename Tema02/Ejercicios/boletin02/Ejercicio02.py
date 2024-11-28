from multiprocessing import Pipe, Process
from random import randint


def generaIps(pipe1):
    for _ in range(1,11):
        num1 = randint(0,255)
        num2 = randint(0,255)
        num3 = randint(0,255)
        num4 = randint(0,255)
        ip = f"{num1}.{num2}.{num3}.{num4}"
        print("Se ha generado la ip: " + ip)
        pipe1.send(ip)

def clasificaIp(pipe2l, pipe2r):
    for _ in range(1,11):
        ip=pipe2l.recv()
        octetos = ip.split(".")
        primero = int(octetos[0])
        if primero >= 0 and primero <= 223:
            print("Se ha enviado " + ip)
            pipe2r.send(ip)
    pipe2r.send(None)

def leeDirecciones(pipe3):
    ip = pipe3.recv()
    while ip is not None:
        octetos = ip.split(".")
        primero = int(octetos[0])
        if primero <= 127:
            clase="A"
        elif primero <= 191:
            clase="B"
        else:
            clase="C"
        print(ip + " es clase " + clase)
        ip = pipe3.recv()


if __name__ == '__main__':
    pipe1, pipe2l = Pipe()
    pipe2r, pipe3 = Pipe()

    pro1 = Process(target=generaIps, args=(pipe1,))
    pro2 = Process(target=clasificaIp, args=(pipe2l, pipe2r))
    pro3 = Process(target=leeDirecciones, args=(pipe3, ))

    pro1.start()
    pro2.start()
    pro3.start()

    pro1.join()
    pro2.join()
    pro3.join()