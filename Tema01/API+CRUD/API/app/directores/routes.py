from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app import directores
from app.ficheros.leer_escribir import leeFichero, escribeFichero

directoresBP = Blueprint('directores', __name__)

ruta = "app/ficheros/directores.json"
rutaSupermercados = "app/ficheros/supermercados.json"


@directoresBP.get('/')
def get_directores():
    directores = leeFichero(ruta)
    return jsonify(directores)


@directoresBP.get("/<int:Id>")
def get_director(Id):
    directores = leeFichero(ruta)
    for director in directores:
        if director['Id'] == Id:
            return director, 200
    return {"error": "director not found"}, 404


@directoresBP.get("/<int:Id>/supermercados")
def get_directores_supermercados(Id):
    list = []
    supermercados = leeFichero(rutaSupermercados)
    for supermercado in supermercados:
        if supermercado['IdDirector'] == Id:
            list.append(supermercado)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No hay supermercados para esa director"}, 404


@directoresBP.post('/')
@jwt_required()
def add_director():
    directores = leeFichero(ruta)
    if request.is_json:
        director = request.get_json(ruta)
        director['Id'] = findNextId()
        directores.append(director)
        escribeFichero(ruta, directores)
        return director, 201
    return {"error": "Request must be json"}, 415

@directoresBP.put("/<int:id>")
@directoresBP.patch("<int:id>")
@jwt_required()
def update_director(id):
    if request.is_json:
        directores = leeFichero(ruta)
        newDirector = request.get_json()
        for director in directores:
            if director["Id"] == id:
                for element in newDirector:
                    director[element] = newDirector[element]
                return newDirector, 200
    return {"error": "Request must be json"}, 415

@directoresBP.delete("/<int:id>")
@jwt_required()
def delete_director(id):
    directores = leeFichero(ruta)
    for director in directores:
        if director["Id"] == id:
            directores.remove(director)
            escribeFichero(ruta,directores)
            return "{}", 200
    return {"error": "Director not found"}, 404


def findNextId():
    directores = leeFichero(ruta)
    return max(director["Id"] for director in directores) + 1
