from pip._vendor import requests
from json import dumps

apiUrl = "http://localhost:5050/"

"""
Muestra todos los directores
"""
def getdirectores():
    urldirectores = apiUrl + "directores"
    response = dumps(requests.get(urldirectores).json(), indent=4)
    return response
"""
Muestra un director
"""
def getdirector(id):
    urldirectores = apiUrl + "directores/" + str(id)
    response = dumps(requests.get(urldirectores).json(), indent=4)
    return response
"""
Muestra las asignaturas que imparte un director
"""
def getdirectorsupermercados(id):
    urldirectores = apiUrl + "directores/" + str(id) + "/supermercados"
    response = dumps(requests.get(urldirectores).json(), indent=4)
    return response

"""
Anade un nuevo director
"""
def postdirector(director, token):
    urlNuevodirector = apiUrl + "directores"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = requests.post(urlNuevodirector, json=director, headers=headers)
    return response

"""
Modifica un director
"""
def putdirector(id, director, token):
    urlModificadirector = apiUrl + "directores/" + str(id)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = str(requests.put(urlModificadirector, json=director, headers=headers).json())
    return response

"""
Borra a un director
"""
def deletedirector(id, token):
    urlBorradirector = apiUrl + "directores/" + str(id)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    response = str(requests.delete(urlBorradirector, headers=headers).json())
    return response

"""
Pregunta datos de un director nuevo
"""
def datosdirector():
    dni = input("Introduce el dni: ")
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    director = {"DNI":dni,"Nombre": nombre, "Apellidos": apellidos,"Email": email}
    return director

"""
Muestra el menu para la gestion de directores
"""
def printMenudirectores():
    print("\n--- Menú ---")
    print("1. Mostrar directores")
    print("2. Buscar un director")
    print("3. Mostrar Supermercados de un director")
    print("4. Añadir director")
    print("5. Actualizar director")
    print("6. Eliminar director")
    print("0. Salir de la aplicación")

"""
funcionalidad del menu de los directores
"""
def menuDirectores(opc, token):
    match opc:
        case "1":
            print(getdirectores())
        case "2":
            id = int(input("Introduce el id del director a buscar: "))
            print(getdirector(id))
        case "3":
            id = int(input("Introduce el id del director: "))
            print(getdirectorsupermercados(id))
        case "4":
            nuevo_director = datosdirector()
            print(postdirector(nuevo_director, token))
        case "5":
            id = int(input("Introduce el id del director a actualizar: "))
            actualiza_director = datosdirector()
            print(putdirector(id, actualiza_director, token))
        case "6":
            id = int(input("Introduce el id del director a borrar: "))
            print(deletedirector(id, token))
        case _:
            print("Opcion invalida")