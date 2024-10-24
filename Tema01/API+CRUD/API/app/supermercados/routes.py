from urllib import request

from flask import Blueprint,jsonify
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
def add_supermercado():
    supermercados = leeFichero(ruta)
    if request.is_json:
        supermercado = request.get_json()
        supermercado['Id'] = findNextId()
        supermercados.append(supermercado)
        escribeFichero(supermercados)
        return supermercado, 201
    return {"error": "Request must be json"}, 415

def findNextId():
    supermercados = leeFichero(ruta)
    return max(supermercado["Id"] for supermercado in supermercados) + 1