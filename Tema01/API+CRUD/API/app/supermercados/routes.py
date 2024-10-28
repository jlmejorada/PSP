from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required


from app import supermercados
from app.ficheros.leer_escribir import *

ruta="app/ficheros/supermercados.json"

supermercadosBP = Blueprint('supermercados', __name__)

@supermercadosBP.get('/')
def get_supermercados():
    supermercados = leeFichero(ruta)
    return jsonify(supermercados)

@supermercadosBP.get("/<int:Id>")
def get_supermercado(Id):
    supermercados = leeFichero(ruta)
    for supermercado in supermercados:
        if supermercado['Id'] == Id:
            return supermercado, 200
    return {"error": "supermercado not found"}, 404

@supermercadosBP.post('/')
@jwt_required()
def add_supermercado():
    supermercados = leeFichero(ruta)
    if request.is_json:
        supermercado = request.get_json()
        supermercado['Id'] = findNextId()
        supermercados.append(supermercado)
        escribeFichero(ruta,supermercados)
        return supermercado, 201
    return {"error": "Request must be json"}, 415

@supermercadosBP.put("/<int:id>")
@supermercadosBP.patch("/<int:id>")
@jwt_required()
def update_supermercado(id):
    if request.is_json:
        supermercados = leeFichero(ruta)
        newSupermercado = request.get_json()
        for supermercado in supermercados:
            if supermercado["Id"] == id:
                for element in newSupermercado:
                    supermercado[element] = newSupermercado[element]
                return newSupermercado, 200
    return {"error": "Request must be json"}, 415

@supermercadosBP.delete("/<int:id>")
@jwt_required()
def delete_supermercados(id):
    supermercados = leeFichero(ruta)
    for supermercado in supermercados:
        if supermercado["Id"] == id:
            supermercados.remove(supermercado)
            escribeFichero(ruta,supermercados)
            return "{}", 200
    return {"error": "Director not found"}, 404

def findNextId():
    supermercados = leeFichero(ruta)
    return max(supermercado["Id"] for supermercado in supermercados) + 1