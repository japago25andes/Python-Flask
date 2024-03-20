from flask import Flask, render_template

app = Flask(__name__)


#filtros personalizados
@app.add_template_filter
def today(date):
    return date.strftime('%d/%m/%Y')

#funciones personalizadas enviadas al html
@app.add_template_global
def repeat(s, n):
    return s * n

from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    name = 'Juan Alejandro Palacios Gómez'
    friends = ['Juan', 'Pedro', 'Pablo', 'Luis']
    date = datetime.now()
    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        date = date
    )

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
    
#prec¿vencion de inyeccion de codigo, se utiliza para convertir a un string plano todo
from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f"Hello, {escape(code)}!"