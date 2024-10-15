# coding: latin1

from flask import *

app = Flask(__name__)

# Lista de directores
directores = [
    {"Id": 1, "DNI": "12345678A", "Nombre": "Carlos", "Apellidos": "P�rez", "email": "carlos.perez@example.com"},
    {"Id": 2, "DNI": "23456789B", "Nombre": "Ana", "Apellidos": "G�mez", "email": "ana.gomez@example.com"},
    {"Id": 3, "DNI": "34567890C", "Nombre": "Miguel", "Apellidos": "Mart�nez", "email": "miguel.martinez@example.com"},
    {"Id": 4, "DNI": "45678901D", "Nombre": "Luc�a", "Apellidos": "Fern�ndez", "email": "lucia.fernandez@example.com"},
    {"Id": 5, "DNI": "56789012E", "Nombre": "David", "Apellidos": "Ruiz", "email": "david.ruiz@example.com"},
    {"Id": 6, "DNI": "67890123F", "Nombre": "Sara", "Apellidos": "Hern�ndez", "email": "sara.hernandez@example.com"},
    {"Id": 7, "DNI": "78901234G", "Nombre": "Jorge", "Apellidos": "L�pez", "email": "jorge.lopez@example.com"},
    {"Id": 8, "DNI": "89012345H", "Nombre": "Elena", "Apellidos": "S�nchez", "email": "elena.sanchez@example.com"},
    {"Id": 9, "DNI": "90123456I", "Nombre": "Fernando", "Apellidos": "Garc�a", "email": "fernando.garcia@example.com"},
    {"Id": 10, "DNI": "01234567J", "Nombre": "Marta", "Apellidos": "Rodr�guez", "email": "marta.rodriguez@example.com"}
]

# Lista de supermercados
supermercados = [
    {"Id": 1, "Fecha": "2020-01-10", "Superficie": 1500, "Direcci�n": "Calle A, 1", "R�gimen": "Propio",
     "IdDirector": 1},
    {"Id": 2, "Fecha": "2021-02-15", "Superficie": 2000, "Direcci�n": "Calle B, 2", "R�gimen": "Franquicia",
     "IdDirector": 2},
    {"Id": 3, "Fecha": "2019-03-20", "Superficie": 1800, "Direcci�n": "Calle C, 3", "R�gimen": "Propio",
     "IdDirector": 3},
    {"Id": 4, "Fecha": "2020-04-25", "Superficie": 2200, "Direcci�n": "Calle D, 4", "R�gimen": "Franquicia",
     "IdDirector": 4},
    {"Id": 5, "Fecha": "2022-05-30", "Superficie": 1700, "Direcci�n": "Calle E, 5", "R�gimen": "Propio",
     "IdDirector": 5},
    {"Id": 6, "Fecha": "2018-06-05", "Superficie": 1900, "Direcci�n": "Calle F, 6", "R�gimen": "Franquicia",
     "IdDirector": 6},
    {"Id": 7, "Fecha": "2020-07-10", "Superficie": 1600, "Direcci�n": "Calle G, 7", "R�gimen": "Propio",
     "IdDirector": 7},
    {"Id": 8, "Fecha": "2021-08-15", "Superficie": 2100, "Direcci�n": "Calle H, 8", "R�gimen": "Franquicia",
     "IdDirector": 8},
    {"Id": 9, "Fecha": "2019-09-20", "Superficie": 2300, "Direcci�n": "Calle I, 9", "R�gimen": "Propio",
     "IdDirector": 9},
    {"Id": 10, "Fecha": "2022-10-25", "Superficie": 2500, "Direcci�n": "Calle J, 10", "R�gimen": "Franquicia",
     "IdDirector": 10}
]


@app.route('/')
def index():
    return 'Hola a todos! uWu'


@app.get("/directores")
def get_directores():
    return jsonify(directores)


@app.get("/directores/<int:id>")
def get_director(id):
    for director in directores:
        if director["Id"] == id:
            return director, 200
        else:
            return {"error": "director not found"}, 404


def findNextIdDir():
    return max(director["Id"] for director in directores) + 1


@app.post("/directores")
def add_director():
    if request.is_json:
        director = request.get_json()
        director["Id"] = findNextIdDir()
        directores.append(director)
        return director, 201
    else:
        return {"error": "Request must be JSON"}, 415

@app.put("/directores/<int:id>")
@app.patch("/directores/<int:id>")
def update_director(id):
    if request.is_json:
        newDirector = request.get_json()
        for director in directores:
            if director["Id"] == id:
                for element in newDirector:
                    director[element] = newDirector[element]
                return 


@app.get("/supermercados")
def get_supermercados():
    return jsonify(supermercados)


@app.get("/supermercados/<int:id>")
def get_supermercado(id):
    for supermercado in supermercados:
        if supermercado["Id"] == id:
            return supermercado, 200
        else:
            return {"error": "supermercado not found"}, 404


def findNextIdSuper():
    return max(supermercado["Id"] for supermercado in supermercados) + 1


@app.post("/supermercados")
def add_supermercado():
    if request.is_json:
        supermercado = request.get_json()
        supermercado["Id"] = findNextIdSuper()
        supermercados.append(supermercado)
        return supermercado, 201
    else:
        return {"error": "Request must be JSON"}, 415

@app.put("/supermercados/<int:id>")
@app.patch("/supermercados/<int:id>")
def update_supermercado(id):
    if request.is_json:
        newSupermercado = request.get_json()
        for supermercado in supermercados:
            if supermercado["Id"] == id:
                for element in newSupermercado:
                    supermercado[element] = newSupermercado[element]
                return

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

