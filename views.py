from main import *
from main import Usuario, _Sessao
from flask import render_template, request

# rotas

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        sessao = _Sessao()
        usuario = Usuario(name=name)
        sessao.add(usuario)
        sessao.commit()
    return render_template('index.html')

@app.route('/remove', methods = ['POST', 'GET'])
def remove():
    if request.method == 'POST':
        name = request.form['name']
        sessao = _Sessao()
        usuario = sessao(name=name)
        if usuario:
            sessao.delete(usuario)
            sessao.commit()
        return render_template('index.html')