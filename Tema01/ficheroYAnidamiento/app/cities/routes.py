from urllib import request

from flask import Blueprint,jsonify

from ficheroYAnidamiento.app import cities
from ficheroYAnidamiento.app.ficheros.leer_escribir import *

ruta="ficheroYAnidamiento/app/ficheros/cities.json"

citiesBP = Blueprint('cities', __name__)

@citiesBP.get('/')
def get_cities():
    cities = leeFichero(ruta)
    return jsonify(cities)

@citiesBP.get("/<int:id>")
def get_city(id):
    cities = leeFichero(ruta)
    for city in cities:
        if city['id'] == id:
            return city, 200
    return {"error": "City not found"}, 404

@citiesBP.post('/')
def add_city():
    cities = leeFichero(ruta)
    if request.is_json:
        city = request.get_json()
        city['id'] = findNextId()
        cities.append(city)
        escribeFichero(cities)
        return city, 201
    return {"error": "Request must be json"}, 415

def findNextId():
    cities = leeFichero(ruta)
    return max(city["id"] for city in cities) + 1