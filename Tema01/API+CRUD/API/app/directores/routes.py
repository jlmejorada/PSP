from flask import Blueprint, jsonify, request
from app.ficheros.leer_escribir import *

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
def add_director():
    directores = leeFichero()
    if request.is_json:
        director = request.get_json(ruta)
        director['Id'] = findNextId()
        directores.append(director)
        escribeFichero(directores)
        return director, 201
    return {"error": "Request must be json"}, 415


def findNextId():
    directores = leeFichero(ruta)
    return max(director["Id"] for director in directores) + 1
