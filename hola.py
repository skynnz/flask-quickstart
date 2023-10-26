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