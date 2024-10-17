from app import app
import json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

def leeFichero():
    archivo = open("fichero.json", "r")
    countries = json.load(archivo)
    archivo.close()
    return countries

def escribeFichero(countries):
    archivo = open("fichero.json", "w")
    json.dump(countries, archivo)
    archivo.close()