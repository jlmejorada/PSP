#coding: latin1

from pip._vendor import requests

apiUrl= ""

## Muestra Men�

def imprimeMenu():
    print("------------------")
    print("-------Men�-------")
    print("------------------")
    print("1.Mostrar director")
    print("2.A�adir director")
    print("3.Actualizar director")
    print("4.Eliminar director")
    print("5.Mostrar supermercado")
    print("6.A�adir supermercado")
    print("7.Actualizar supermercado")
    print("8.Eliminar supermercado")
    print("------------------")
    print("Dime una opci�n:")

## Muestra director
def muestraDirector():
    urlPosts = apiUrl + "directores"
    response = str(requests.get(urlPosts).json())

    return response

## Muestra supermercado
def muestraSupermercado():
    urlPosts = apiUrl + "supermercados"
    response = str(requests.get(urlPosts).json())

    return response

## A�ade director
def anadeDirector(id, dni, nombre, apellidos, email):
    urlPosts = apiUrl + "director"
    todo = {'Id':id, 'dni': dni, 'nombre': nombre, 'apellidos': apellidos, 'email': email}

    response = requests.post(urlPosts, json=todo)
    print(response.json())
    print(response.status_code)

## A�ade Supermercado
def anadeSupermercado(id, fecha, superficie, direcci�n, regimen, idDirector):
    urlPosts = apiUrl + "supermercado"
    todo = {'Id':id, 'Fecha': fecha, 'Superficie': superficie, 'Direcci�n': direcci�n, 'Regimen': regimen, 'IdDirector': idDirector}

    response = requests.post(urlPosts, json=todo)
    print(response.json())
    print(response.status_code)

## Eliminar director
def eliminaDirector():
    urlPosts = apiUrl + "directores"
    response = str(requests.delete(urlPosts).json())

    return response

## Eliminar supermercado
def eliminaSupermercado():
    urlPosts = apiUrl + "supermercados"
    response = str(requests.delete(urlPosts).json())

    return response

## Modificar director
def anadeDirector(id, dni, nombre, apellidos, email):
    urlPosts = apiUrl + "director"
    todo = {'Id':id, 'dni': dni, 'nombre': nombre, 'apellidos': apellidos, 'email': email}

    response = requests.put(urlPosts, json=todo)
    print(response.json())
    print(response.status_code)

## Modificar Supermercado
def anadeSupermercado(id, fecha, superficie, direcci�n, regimen, idDirector):
    urlPosts = apiUrl + "supermercado"
    todo = {'Id':id, 'Fecha': fecha, 'Superficie': superficie, 'Direcci�n': direcci�n, 'Regimen': regimen, 'IdDirector': idDirector}

    response = requests.put(urlPosts, json=todo)
    print(response.json())
    print(response.status_code)