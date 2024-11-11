from flask import Flask

from app.usuario.routes import usuariosBP
from app.vehiculo.routes import vehiculoBP
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.register_blueprint(vehiculoBP, url_prefix='/vehiculo')

app.register_blueprint(usuariosBP, url_prefix='/usuarios')

app.config["JWT_SECRET_KEY"] = 'tu_clave'
jwt = JWTManager(app)