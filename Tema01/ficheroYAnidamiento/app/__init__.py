from flask import Flask
from .countries.routes import countriesBP
from .cities.routes import citiesBP
from .users.routes import usersBP
app = Flask(__name__)
app.register_blueprint(countriesBP, url_prefix='/countries')
app.register_blueprint(citiesBP, url_prefix='/cities')
app.register_blueprint(usersBP, url_prefix='/users')

