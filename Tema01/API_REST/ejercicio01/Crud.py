#coding: latin1

from pip._vendor import requests

apiUrl= "http://localhost:5050/"

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

## Añade director
def anadeDirector(id, dni, nombre, apellidos, email):
    urlPosts = apiUrl + "director"
    todo = {'Id':id, 'dni': dni, 'nombre': nombre, 'apellidos': apellidos, 'email': email}

    response = requests.post(urlPosts, json=todo)
    print(response.json())
    print(response.status_code)

## Añade Supermercado
def anadeSupermercado(id, fecha, superficie, dirección, regimen, idDirector):
    urlPosts = apiUrl + "supermercado"
    todo = {'Id':id, 'Fecha': fecha, 'Superficie': superficie, 'Dirección': dirección, 'Regimen': regimen, 'IdDirector': idDirector}

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
def anadeSupermercado(id, fecha, superficie, dirección, regimen, idDirector):
    urlPosts = apiUrl + "supermercado"
    todo = {'Id':id, 'Fecha': fecha, 'Superficie': superficie, 'Dirección': dirección, 'Regimen': regimen, 'IdDirector': idDirector}

    response = requests.put(urlPosts, json=todo)
    print(response.json())
    print(response.status_code)