#--------- SCRIPT API AUTORES - PARTE COLADA NO app_01.py

from flask import Flask, jsonify, request
from schema_db_02 import Autor, Postagem, app, db
import json
import requests

#app = Flask(__name__) utilizaremos o app e db do schema

@app.route('/autores')
def obter_autores():
    autores = Autor.query.all()         #chama toda a tabela
    lista_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_autores.append(autor_atual)

    return jsonify({'autores':lista_autores},200)

@app.route('/autores/<int:id_autor>', methods = ['GET'])
def obter_autores_id():
    

@app.route('/autores', methods = ['POST'])
def inserir_autores(id_autor):
    pass

@app.route('/autores/<int:id_autor>', methods = ['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>', methods = ['DELETE'])
def deletar_autor_id(id_autor):
    pass

if __name__ == '__main__':
    app.run(port=5000, host= 'localhost', debug=True)

