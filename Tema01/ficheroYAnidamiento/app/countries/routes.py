from flask import Blueprint, jsonify, request

from ficheroYAnidamiento.app import cities
from ficheroYAnidamiento.app.ficheros.leer_escribir import escribeFichero, leeFichero
from ficheroYAnidamiento.app.ficheros.leer_escribir import escribeFichero, leeFichero
from flaskProject.app import findNextId, countries

countriesBP = Blueprint('countries', __name__)

ruta="ficheroYAnidamiento/app/ficheros/countries.json"
rutaCities="ficheroYAnidamiento/app/ficheros/cities.json"

@countriesBP.get('/')
def get_countries():
    countries = leeFichero(ruta)
    return jsonify(countries)

@countriesBP.get("/<int:id>")
def get_country(id):
    countries = leeFichero(ruta)
    for country in countries:
        if country['id'] == id:
            return country, 200
    return {"error": "Country not found"}, 404

@countriesBP.get("/<int:id>/cities")
def get_countries_cities(id):
    list = []
    cities = leeFichero(rutaCities)
    for city in cities:
        if city['idCountry'] == id:
            list.append(city)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No hay cities para esa country"}, 404

@countriesBP.post('/')
def add_country():
    countries = leeFichero()
    if request.is_json:
        country = request.get_json(ruta)
        country['id'] = findNextId()
        countries.append(country)
        escribeFichero(countries)
        return country, 201
    return {"error": "Request must be json"}, 415

def findNextId():
    countries = leeFichero(ruta)
    return max(country["id"] for country in countries) + 1