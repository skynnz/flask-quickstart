from flask import Flask

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