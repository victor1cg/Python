
#! API Flask - Get com ID
from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)
postagens = [
    {
        "titulo":"Minha historia",
        "autor":"Amanda Dias"
    },
    {
        "titulo":"Novo dispositivo Sony",
        "autor":"Howard Stringer"
    },
    {
        "titulo":"Lancamento do Ano",
        "autor":"Jeff Bezos"
    }
]   

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

if __name__ == '__main__':
    app.run(port=5000, host= 'localhost', debug=True)
