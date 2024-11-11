from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.ficheros.leer_escribir import *

#Creamos un Blueprint para facilitar el uso de las clases
vehiculoBP = Blueprint('vehiculo', __name__)
#Guardamos la ruta de nuestro Json vehiculo
ruta = "app/ficheros/vehiculos.json"

#Función que devuelve la lista entera de vehiculos
@vehiculoBP.get('/')
@jwt_required()
def get_vehiculos():
    vehiculos = leeFichero(ruta)
    return jsonify(vehiculos)

# Funcion que devuelve un vehiculo buscado por su id
@vehiculoBP.get("/<int:id>")
@jwt_required()
def get_vehiculo(id):
    vehiculos = leeFichero(ruta)
    for vehiculo in vehiculos:
        if vehiculo['id'] == id:
            return vehiculo, 200
    return {"error": "vehiculo not found"}, 404

# Añade un objeto json vehiculo con un id nuevo y en el estado pendiente por defecto
@vehiculoBP.post('/')
@jwt_required()
def add_vehiculo():
    vehiculos = leeFichero(ruta)
    if request.is_json:
        vehiculo = request.get_json(ruta)
        if vehiculo['matricula'] is not None and vehiculo['marca'] is not None and vehiculo['modelo'] is not None:
            vehiculo['id'] = findNextId()
            vehiculo['estado'] = "pendiente"
            vehiculos.append(vehiculo)
            escribeFichero(ruta, vehiculos)
            return vehiculo, 201
        return {"error": "Vehiculo must have a matricula, marca and modelo"}, 400
    return {"error": "Request must be json"}, 415

# Modifica un vehiculo buscado por su id
@vehiculoBP.put("/<int:id>")
@vehiculoBP.patch("<int:id>")
@jwt_required()
def update_vehiculo(id):
    if request.is_json:
        vehiculos = leeFichero(ruta)
        newVehiculo = request.get_json()
        for vehiculo in vehiculos:
            if vehiculo["id"] == id:
                for element in newVehiculo:
                    vehiculo[element] = newVehiculo[element]
                    escribeFichero(ruta, vehiculos)
                return newVehiculo, 200
    return {"error": "Request must be json"}, 415

# Borra un vehiculo buscado por su id
@vehiculoBP.delete("/<int:id>")
@jwt_required()
def delete_vehiculo(id):
    vehiculos = leeFichero(ruta)
    for vehiculo in vehiculos:
        if vehiculo["id"] == id:
            vehiculos.remove(vehiculo)
            escribeFichero(ruta,vehiculos)
            return "{}", 200
    return {"error": "Vehiculo not found"}, 404

# Busca cual fue la ultima ID asignada y devuelve está más 1
def findNextId():
    vehiculos = leeFichero(ruta)
    return max(vehiculo["id"] for vehiculo in vehiculos) + 1