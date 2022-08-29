
#! API Flask

from flask import Flask, jsonify, request
from schema_db_02 import Autor, Postagem, app, db
import json

#app = Flask(__name__)

#* ---------- POSTAGENS -------------
@app.route('/')
def obter_postagens():
    return jsonify (postagens)

#* GET com indice;
@app.route('/postagens/<int:indice>', methods = ['GET']) #somente o metodo GET
def obter_postagem_id(indice):
    return jsonify(postagens[indice])

#* Criar uma nova postagem - POST;
@app.route('/postagem',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()       #os dados serão incluidos via Postman, recurso Flask
    postagens.append(postagem)

    return (postagem,200)               #(json, status code de OK)

@app.route('/postagem/<int:indice>',methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}',200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão',404)

#* ---------- AUTORES -------------
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
def obter_autores_id(id_autor):
    autor = Autor.query.filter_by(id_autor = id_autor).first()
    if not autor:
        return jsonify(f'Autor nao encontrado! ')
    
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    return jsonify(f'Voce buscou pelo autor: {autor_atual}')
    

@app.route('/autores', methods = ['POST'])
def inserir_autores():
    novo_autor = request.get_json()
    autor = Autor(nome = novo_autor['nome'], email = novo_autor['email'], senha = novo_autor['senha'])
    
    #salvar no db e gravar
    db.session.add(autor)
    db.session.commit()
    return jsonify({'Usuario cadastrado com sucesso',200})


@app.route('/autores/<int:id_autor>', methods = ['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>', methods = ['DELETE'])
def deletar_autor_id(id_autor):
    pass

if __name__ == '__main__':
    app.run(port=5000, host= 'localhost', debug=True)