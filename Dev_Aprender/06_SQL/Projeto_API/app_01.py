
#! API Flask

from datetime import datetime
from tkinter import EXCEPTION
from flask import Flask, jsonify, request, make_response
from schema_db_02 import Autor, Postagem, app, db
import json
import jwt
from datetime import datetime, timedelta
from functools import wraps
#Rota padrão - GET https://localhost:5000


#* ---------- TOKEN OBRIGATORIO -------------
def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Verificar se um token foi enviado
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'mensagem': 'Token não foi incluído!'}, 401)
        # Se temos um token, validar acesso consultando o BD
        try:
            resultado = jwt.decode(token,app.config['SECRETE_KEY'],algorithms=["HS256"])
            autor = Autor.query.filter_by(
                id_autor=resultado['id_autor']).first()
        except:
            return jsonify({'mensagem': 'Token é inválido'}, 401)
        return f(autor, *args, **kwargs)
    return decorated

#*------------ LOGIN / TOKEN -------------
# verificar se o login é valido - make_response adding additional HTTP headers.
# dentro da tabela Autor(blog.db) temos usuario e senha
@app.route('/login',methods = ['GET'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    usuario = Autor.query.filter_by(nome=auth.username).first()
   
    if not usuario:
        return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    
    if auth.password == usuario.senha:
        token = jwt.encode({'id_autor': usuario.id_autor, 'exp': datetime.utcnow() + timedelta(minutes=30)},app.config['SECRETE_KEY'])
        return jsonify({'token':str(token)})
    
    return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})

#* ---------- POSTAGENS -------------
@app.route('/')
@token_obrigatorio
def obter_postagens(autor):
    postagem = Postagem.query.all()

    list_postagens = []
    for post in postagem:
        postagem_atual = {}
        postagem_atual['id_postagem'] = post.id_postagem
        postagem_atual['titulo'] = post.titulo
        postagem_atual['id_autor'] = post.id_autor
        list_postagens.append(postagem_atual)
    return jsonify ({'postagens': list_postagens})

#* GET com indice;
@app.route('/postagens/<int:indice>', methods = ['GET']) #somente o metodo GET
@token_obrigatorio
def obter_postagem_por_indice(autor, id_postagem):
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    postagem_atual = {}
    try:
        postagem_atual['titulo'] = postagem.titulo
    except:
        pass
    postagem_atual['id_autor'] = postagem.id_autor

    return jsonify({'postagens': postagem_atual})

#* Criar uma nova postagem - POST;
@app.route('/postagem',methods=['POST'])
@token_obrigatorio
def nova_postagem(autor):
    nova_postagem = request.get_json()
    postagem = Postagem(
        titulo=nova_postagem['titulo'], id_autor=nova_postagem['id_autor'])

    db.session.add(postagem)
    db.session.commit()
    return jsonify({'mensagem': 'Postagem criada com sucesso'})


@app.route('/postagem/<int:id_postagem>',methods=['PUT'])
@token_obrigatorio
def alterar_postagem(autor, id_postagem):
    postagem_alterada = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    try:
        postagem.titulo = postagem_alterada['titulo']
    except:
        pass
    try:
        postagem.id_autor = postagem_alterada['id_autor']
    except:
        pass
    db.session.commit()
    return jsonify({'mensagem': 'Postagem alterada com sucessso'})


@app.route('/postagem/<int:id_postagem>',methods=['DELETE'])
@token_obrigatorio
def excluir_postagem(autor, id_postagem):
    postagem_a_ser_excluida = Postagem.query.filter_by(
        id_postagem=id_postagem).first()
    if not postagem_a_ser_excluida:
        return jsonify({'mensagem': 'Não foi encontrado uma postagem com este id'})
    db.session.delete(postagem_a_ser_excluida)
    db.session.commit()

    return jsonify({'mensagem': 'Postagem excluída com sucesso!'})

#* ---------- AUTORES -------------

@app.route('/autores')
@token_obrigatorio
def obter_autores(autor):
    autores = Autor.query.all()         #chama toda a tabela
    lista_autores = []
    for autor in autores:
        autor_atual = {}                #popular é preencher com informações
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_autores.append(autor_atual)

    return jsonify({'autores':lista_autores},200)

@app.route('/autores/<int:id_autor>', methods = ['GET'])
@token_obrigatorio
def obter_autores_id(autor,id_autor):
    autor = Autor.query.filter_by(id_autor = id_autor).first()
    if not autor:
        return jsonify(f'Autor nao encontrado! ')
    
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    return jsonify(f'Voce buscou pelo autor: {autor_atual}')
    

@app.route('/autores', methods = ['POST'])
@token_obrigatorio
def inserir_autores(autor):
    novo_autor = request.get_json()
    autor = Autor(nome = novo_autor['nome'], senha = novo_autor['senha'],email = novo_autor['email'])
    
    #salvar no db e gravar
    db.session.add(autor)
    db.session.commit()
    return jsonify({'Autor cadastrado com sucesso',200})


@app.route('/autores/<int:id_autor>', methods = ['PUT'])
@token_obrigatorio
def alterar_autor(autor,id_autor):
    usuario_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor = id_autor).first()
    if not Autor:
        return jsonify({'Autor não encontrado ! '})
    
    #Verificar os dados a alterar, caso não encontre continua (try,except)
    try:
        usuario_alterar['nome']
        autor.nome = usuario_alterar['nome']
    except:
        pass
    try:
        usuario_alterar['email']
        autor.email = usuario_alterar['email']
    except:
        pass
    try:    
        usuario_alterar['senha']
        autor.senha = usuario_alterar['senha']
    except:
        pass

    db.session.commit()
    return jsonify({'Autor alterado com sucesso'},200)


@app.route('/autores/<int:id_autor>', methods = ['DELETE'])
@token_obrigatorio
def deletar_autor_id(autor,id_autor):
    autor_deletar = Autor.query.filter_by(id_autor = id_autor).first()
    if not Autor:
        return jsonify({'Autor não encontrado'},200)
    
    db.session.delete(autor_deletar)
    db.session.commit()    
    return jsonify({'Autor Excluido ! '},200)



if __name__ == '__main__':
    app.run(port=5000, host= 'localhost', debug=True)