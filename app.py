"""
Script controlador del backend MVC de mi plataforma web
Autor: JSalazar
Fecha: 15/Sep/2022
"""

#Incluimos los modulos a utilizar del framework flask
from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL #Modulo de compatibilidad sql
from pymysql.cursors import DictCursor #Importar un cursor sql
from datetime import datetime #Modulo para saber la fecha y hora
import re #Importamos modulo re

#Creamos un objeto app de flask
app = Flask(__name__)

#Configuramos una llave secreta para proteccion extra
app.secret_key = 'levelup'

#Declaramos la conexion sql
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #Configuramos la direccion del servidor
app.config['MYSQL_DATABASE_USER'] = 'root' #Usuario con acceso a la bd
app.config['MYSQL_DATABASE_PASSWORD'] = '' #Password del usuario con acceso a la bd
app.config['MYSQL_DATABASE_DB'] = 'levelup' #Nombre de la bd a conectar

#Creamos un cursor para recorrer las tablas de la bd
mysql = MySQL(app, cursorclass = DictCursor)

"""
---------- Comienzan las rutas de urls de la app (controlador de vistas) ----------
"""

#Vista para el error 404 not found
@app.route('/404')
def error404():
    #Data es la informacion que le vamos a enviar a la plantilla al cargar(renderizar) esta url 
    data = {
        'titulo' : 'BookShelf' #Titulo a mostrar en la pestana del navegador
    }
    return render_template('404.html', data = data)

#Vista principal (index) mostramos como index el login.html
@app.route('/', methods=['GET', 'POST'])
def login():
    #Variable que contiene los datos a configurar en la plantilla html
    data = {
        'titulo' : 'Bookshelf - Inicio de Sesion'
    }
    return render_template('login.html', data = data)


#Ejecutamos la aplicacion
if __name__ == '__main__':
    app.run(debug = True, port = 5000)