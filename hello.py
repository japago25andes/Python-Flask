from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

#string
#int
#float
#path === para poder recibir cadenas de caracteres con caracteres especiales
#uuid
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name = None, age = None):
    if name is None and age is None:
        return "Hello, World!"
    elif age is None:
        return f"Hello, {name}!"
    else:
        return f"Hello, {name}  {age * 5}!"