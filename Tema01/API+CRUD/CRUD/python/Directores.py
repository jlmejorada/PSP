from pip._vendor import requests

apiUrl = "http://localhost:5050/"

"""
Muestra todos los directores
"""
def getdirectores():
    urldirectores = apiUrl + "directores"
    response = str(requests.get(urldirectores).json())
    return response
"""
Muestra un director
"""
def getdirector(id):
    urldirectores = apiUrl + "directores/" + str(id)
    response = str(requests.get(urldirectores).json())
    return response
"""
Muestra las asignaturas que imparte un director
"""
def getdirectorAsignaturas(id):
    urldirectores = apiUrl + "directores/" + str(id) + "/asignaturas"
    response = str(requests.get(urldirectores).json())
    return response

"""
Anade un nuevo director
"""
def postdirector(director):
    urlNuevodirector = apiUrl + "directores"
    response = requests.post(urlNuevodirector, json=director)
    return response

"""
Modifica un director
"""
def putdirector(id, director):
    urlModificadirector = apiUrl + "directores/" + str(id)
    response = str(requests.put(urlModificadirector, json=director).json())
    return response

"""
Borra a un director
"""
def deletedirector(id):
    urlBorradirector = apiUrl + "directores/" + str(id)
    response = str(requests.delete(urlBorradirector).json())
    return response

"""
Pregunta datos de un director nuevo
"""
def datosdirector():
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce el apellidos: ")
    telefono = input("Introduce el telefono: ")
    direccion = input("Introduce el direccion: ")
    cc = input("Introduce el Cuenta Bancaria: ")
    director = {"nombre": nombre, "apellidos": apellidos, "telefono": telefono, "direccion": direccion,"cc": cc}
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
def menuDirectores(opc):
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
            print(postdirector(nuevo_director))
        case "5":
            id = int(input("Introduce el id del director a actualizar: "))
            actualiza_director = datosdirector()
            print(putdirector(id, actualiza_director))
        case "6":
            id = int(input("Introduce el id del director a borrar: "))
            print(deletedirector(id))
        case _:
            print("Opcion invalida")