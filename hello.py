from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/user/<name>')
def hello(name):
    return f"Hello, {name}!"