# Python-Flask
## Herramientas Necesarias

* python -V
* pip -V
* pip install virtualenv

## Configuracion Inicial

1. Crear un directorio y movernos alli para inicial el proyecto
2. Crear el ambiente virtual, para este caso "py -m venv env"
3. Verificar que la carpeta con el nombre del entorno este creada
4. Activar el entorno de trabajo "env\scripts\activate"
5. Instala flask "pip install flask"
6. Verificar las dependencias que estan instaladas "pip freeze" o "pip list"
7. Crear el archivo de requerimientos para no tener que instalar con pip siempre "echo. > requirements.txt"
8. Para instalar con el archivo "requirements.txt" => utilizar "pip install -r requirements.txt"
9. Crear el archivo main "echo. > main.py"
10. Escribir codigo.
11. Si queremos desactivar el entorno: deactivate

## Iniciar el servidor de Flask

1. Configurar la variable de entorno para que encuentre la aplicacion "set FLASK_APP=main.py"
2. Correo el servidor de Flask "flask run"

-----

1. Comando para iniciael servidor sin cambiar la variable de entorno: "flask --app hello run"
2. Modo depurador: "flask --app hello --debug run"