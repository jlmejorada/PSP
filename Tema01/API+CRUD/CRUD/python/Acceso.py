import requests


def login():
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")
    response = requests.get("http://localhost:5050/usuarios", json={"Usuario": usuario, "Contrasena": contrasena})

    if response.status_code == 200:
        token = response.json().get("token")
        return token

    else:
        print("Pon bien la contraseña")
        login()