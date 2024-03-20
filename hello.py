from flask import Flask, render_template, url_for

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
def index():

    print(url_for('index'))
    print(url_for('hello', name = 'Juan', age = 25))
    print(url_for('code', code = 'Juan Palacios'))

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
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data = my_data)
    
#prec¿vencion de inyeccion de codigo, se utiliza para convertir a un string plano todo
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f"Hello, {escape(code)}!"