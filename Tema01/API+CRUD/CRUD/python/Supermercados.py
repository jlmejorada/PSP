from pip._vendor import requests

apiUrl = "http://localhost:5050/"

"""
Muestra todos los supermercados
"""
def getsupermercados():
    urlsupermercados = apiUrl + "supermercados"
    response = str(requests.get(urlsupermercados).json())
    return response
"""
Muestra un supermercado
"""
def getsupermercado(id):
    urlsupermercado = apiUrl + "supermercados/" + str(id)
    response = str(requests.get(urlsupermercado).json())
    return response
"""
Anade un supermercado
"""
def postsupermercado(supermercado):
    urlNuevasupermercado = apiUrl + "supermercados"
    response = requests.post(urlNuevasupermercado, json=supermercado)
    return response
"""
Modifica un supermercado
"""
def putsupermercado(id, supermercado):
    urlModificasupermercado = apiUrl + "supermercados/" + str(id)
    response = str(requests.put(urlModificasupermercado, json=supermercado).json())
    return response
"""
Borra un supermercado
"""
def deletesupermercado(id):
    urlBorrasupermercado = apiUrl + "supermercados/" + str(id)
    response = str(requests.delete(urlBorrasupermercado).json())
    return response
"""
Pregunta datos de un supermercado
"""
def datossupermercado():
    titulo = input("Introduce el nombre: ")
    numHoras = input("Introduce el numero de horas: ")
    idProfesor = input("Introduce el id del profesor que la imparte: ")
    supermercado = {"titulo": titulo, "numHoras": numHoras, "idProfesor": idProfesor}
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
def menuSupermercados(opc):
    match opc:
        case "1":
            print(getsupermercados())
        case "2":
            id = int(input("Introduce el id del supermercado: "))
            print(getsupermercado(id))
        case "3":
            nueva_supermercado = datossupermercado()
            print(postsupermercado(nueva_supermercado))
        case "4":
            id = int(input("Introduce el id del supermercado a modificar: "))
            actualiza_supermercado = datossupermercado()
            print(putsupermercado(id, actualiza_supermercado))
        case "5":
            id = int(input("Introduce el id del supermercado a borrar: "))
            print(deletesupermercado(id))
        case _:
            print("Opcion invalida")