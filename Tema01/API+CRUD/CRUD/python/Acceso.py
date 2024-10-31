import requests


def login():
    usuario=input("Ingrese usuario: ")
    contrasena=input("Ingrese contraseña: ")
    token=requests.get("http://localhost:5050/usuarios").json()
    return token