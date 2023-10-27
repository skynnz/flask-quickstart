from flask import Flask, render_template
from markupsafe import escape
from markupsafe import Markup

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "<p>Hola, Mundo!</p>"

@app.route("/titulo-h2")
def titulo_h2():
    return "<h1>Hola, soy un titulo</h1>"

@app.route("/parrafo")
def parrafo():
    return "<p>Hola, soy un parrafo</p>"

@app.route("/get-lista")
def lista():
    GetLista = ["administrador de sistemas", "secretaria", "gerente", "vendedor", "auxiliar de compra"]
    return(GetLista)

@app.route("/get-diccionario")
def diccionario():
    GetDiccionario = {
        "id":"36",
        "nombres":"Justo",
        "apellidos": "Rojas",
        "edad": "64",
        "fechanac": "1960-06-01",
    }
    return(GetDiccionario)

@app.route("/persona-cedula/<cedula>")
def var_persona(cedula):
    d = {
        "persona":"Claudia",
        "cedula": cedula,
    }
    return f'La cedula es, {escape(str(d))}'

@app.route("/verificar-edad/<int:edad>")
def verificar_edad(edad):
    if edad >= 18:
        return "La persona es mayor de edad."
    else:
        return "La persona es menor de edad."

""" Crear un endpoint que reciba 2 parámetros y muestre su resultado al navegador """
@app.route("/parametros/<parametro1>/<parametro2>")
def verif_param(parametro1, parametro2):
    return f'Los parametros son {parametro1, parametro2}'

"plantillas con jinja"
@app.route('/index/<name>')
def index(name=None):
    return render_template('index.html', name=name)