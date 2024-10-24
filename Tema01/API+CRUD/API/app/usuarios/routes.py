import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from app.ficheros.leer_escribir import leeFichero, escribeFichero

ficheroUsuarios = "/app/ficheros/usuarios.json"
usuariosBP = Blueprint('usarios', __name__)

@usuariosBP.post('/')
def registroUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        nuevo_usuario = request.get_json()
        contrasena = nuevo_usuario['Contrasena'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashContrasena = bcrypt.hashpw(contrasena, salt).hex()
        nuevo_usuario['Contrasena'] = hashContrasena
        usuarios.append(nuevo_usuario)
        escribeFichero(ficheroUsuarios, usuarios)
        token = create_access_token(identity= nuevo_usuario ["Usuario"])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415