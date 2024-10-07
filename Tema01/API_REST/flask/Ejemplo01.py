from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola a todos! uwu'

if __name__ == '__name__':
    app.run(deubg=True, host='0.0.0.0', port=6666)