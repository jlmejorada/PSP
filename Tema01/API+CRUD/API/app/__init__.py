from flask import Flask
from .directores.routes import directoresBP
from .supermercados.routes import supermercadosBP
from .usuarios.routes import usuariosBP
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.register_blueprint(directoresBP, url_prefix='/directores')
app.register_blueprint(supermercadosBP, url_prefix='/supermercados')
app.register_blueprint(usuariosBP, url_prefix='/usuarios')

app.config["SECRET_KEY"] = 'tu_clave'
jwt = JWTManager(app)