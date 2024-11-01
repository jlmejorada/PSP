from pip._vendor import requests
from json import dumps

apiUrl = "http://localhost:5050/"

"""
Muestra todos los supermercados
"""
def getsupermercados():
    urlsupermercados = apiUrl + "supermercados"
    response = dumps(requests.get(urlsupermercados).json(), indent=2)
    return response
"""
Muestra un supermercado
"""
def getsupermercado(id):
    urlsupermercado = apiUrl + "supermercados/" + str(id)
    response = dumps(requests.get(urlsupermercado).json(), indent=2)
    return response
"""
Anade un supermercado
"""
def postsupermercado(supermercado, token):
    urlNuevosupermercado = apiUrl + "supermercados"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = requests.post(urlNuevosupermercado, json=supermercado, headers=headers)
    return response
"""
Modifica un supermercado
"""
def putsupermercado(id, supermercado, token):
    urlModificasupermercado = apiUrl + "supermercados/" + str(id)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = str(requests.put(urlModificasupermercado, json=supermercado, headers=headers).json())
    return response
"""
Borra un supermercado
"""
def deletesupermercado(id, token):
    urlBorrasupermercado = apiUrl + "supermercados/" + str(id)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = str(requests.delete(urlBorrasupermercado, headers).json())
    return response
"""
Pregunta datos de un supermercado
"""
def datossupermercado():
    fecha = input("Introduce la fecha: ")
    superficie = input("Introduce la superficie: ")
    direccion = input("Introduce la dirección: ")
    regimen = input("Introduce el regimen: ")
    idDirector = input("Introduce el id del director que la dirige: ")
    supermercado = {"Fecha": fecha, "Superficie": superficie, "Direccion":direccion, "Regimen": regimen, "IdDirector": idDirector}
    return supermercado

"""
Muestra el menu para la gestion de supermercados
"""
def printMenusupermercados():
    print("\n--- Menú ---")
    print("1. Mostrar supermercados ")
    print("2. Buscar un supermercado ")
    print("3. Añadir supermercado ")
    print("4. Actualizar supermercado ")
    print("5. Eliminar supermercado")
    print("0. Salir de la aplicación")

"""
Funcionalidad del menu de las supermercados
"""
def menuSupermercados(opc, token):
    match opc:
        case "1":
            print(getsupermercados())
        case "2":
            id = int(input("Introduce el id del supermercado: "))
            print(getsupermercado(id))
        case "3":
            nueva_supermercado = datossupermercado()
            print(postsupermercado(nueva_supermercado, token))
        case "4":
            id = int(input("Introduce el id del supermercado a modificar: "))
            actualiza_supermercado = datossupermercado()
            print(putsupermercado(id, actualiza_supermercado, token))
        case "5":
            id = int(input("Introduce el id del supermercado a borrar: "))
            print(deletesupermercado(id, token))
        case _:
            print("Opcion invalida")