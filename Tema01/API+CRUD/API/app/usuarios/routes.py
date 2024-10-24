from flask import Blueprint, request


ficheroUsuarios = "/app/ficheros/usuarios.json"

usuariosBP = Blueprint('usarios', __name__)