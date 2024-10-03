#coding: latin1
from urllib import response
from xmlrpc.client import boolean
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/"
idTodo = int(input("Dime un id\n"))
title = str(input("Dime una tarea\n"))
completed = bool(input("Está acabada? (Responde True o False)\n"))

todo = {"userId": idTodo, "title" : title, "completed": completed}
response = requests.post(api_url, json=todo)

print(response.json())

print("Código de estado: ", response.status_code)