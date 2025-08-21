from main import app
from main import *
from main import Usuario, _Sessao
from flask import render_template, request

# rotas

@app.route('/')
def index():
    sessao = _Sessao()
    usuarios = sessao.query(Usuario)
    return render_template('index.html', usuarios=usuarios)

@app.route('/create', methods=['POST', 'GET'])
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
        usuario = sessao.query(Usuario).filter_by(name=name).first()
        if usuario:
            sessao.delete(usuario)
            sessao.commit()
        return render_template('index.html')

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        sessao = _Sessao()
        usuario = sessao.query(Usuario).filter_by(name=name).first()
        if usuario:
            usuario.name = request.form['new_name']
            sessao.commit()
        return render_template('index.html')
    
# @app.route('/read')
# def read():
#     name = Usuario(name)
#     sessao = _Sessao()
#     usuario = sessao.query(Usuario).filter_by(name=name).first()
#     for conta in usuario:
#         lista = list[conta]
#         return render_template('index.html', lista)
    