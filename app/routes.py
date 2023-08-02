from app import app
from flask import render_template
from app.forms import Contato

@app.route('/')
def index():
    return render_template("index.html",title="Bem Vindo")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html",title="sobre mim")

@app.route('/contato')
def contato():
    return render_template("contato.html",title="contato")

@app.route('/projeto')
def projeto():
    return render_template("projeto.html",title="projeto")

@app.route('/enviar-contato')
def enviar():
    formulario= Contato()
    return render_template("enviar.html",title="projeto")