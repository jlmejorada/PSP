from flask import *

app = Flask(__name__)
@app.route('/')

def index():
    return 'Hola a todos! uwu'

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5050)