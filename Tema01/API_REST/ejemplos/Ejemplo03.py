#coding: latin1
from urllib import response
from pip._vendor import requests
apiUrl = "https://jsonplaceholder.typicode.com/todos/10"

# Petici�n GET
response = requests.get(apiUrl)
print(response.json())

# Construimos el diccionario con los datos a modificar
todo = {'userId':1, 'title': 'Wash car', 'completed': True}

# Realizamos petici�n PUT
response = requests.put(apiUrl, json=todo)
print(response.json())
print(response.status_code)
