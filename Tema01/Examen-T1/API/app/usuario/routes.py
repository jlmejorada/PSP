import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from app.ficheros.leer_escribir import leeFichero, escribeFichero

ficheroUsuarios = "app/ficheros/usuarios.json"
usuariosBP = Blueprint('usuarios', __name__)

@usuariosBP.post('/')
def registroUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        contrasena = usuario['contrasena'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashContrasena = bcrypt.hashpw(contrasena, salt).hex()
        usuario['contrasena'] = hashContrasena
        usuarios.append(usuario)
        escribeFichero(ficheroUsuarios, usuarios)
        token = create_access_token(identity= usuario["usuario"])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415

@usuariosBP.get('/')
def loginUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        nomUsuario = usuario['usuario']
        contUsuario = usuario['contrasena'].encode('utf-8')
        for archivoUsuario in usuarios:
            if archivoUsuario['usuario'] == nomUsuario:
                archivoContrasena = archivoUsuario['contrasena']
                if bcrypt.checkpw(contUsuario, bytes.fromhex(archivoContrasena)):
                    token = create_access_token(identity= nomUsuario)
                    return {'token': token}, 200
                else:
                    return {'error': 'No authorized'}, 401
        return {'error': 'User not found'}, 404
    return {"error": "Request must be JSON"}, 415


