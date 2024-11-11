import json

def leeFichero(ruta):
    archivo = open(ruta, "r")
    objeto = json.load(archivo)
    archivo.close()
    return objeto

def escribeFichero(ruta,objeto):
    archivo = open(ruta, "w")
    json.dump(objeto, archivo)
    archivo.close()