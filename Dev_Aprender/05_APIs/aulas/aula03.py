
#! Criando nossa primeira API

# Frameworks mais utilizados - Flask e Django

from flask import Flask, jsonify, request

# *Flask - object que criará uma função que retorna uma resposta HTTP - Criar um webserver em menos de 7 linhas
''' 
@app.route é um decorador que transforma uma função Python comum em uma função de visualização Flask. Ela converte o valor de retorno da função em uma resposta HTTP para ser mostrada por um cliente HTTP, como um navegador Web. Passe o valor '/' para @app.route() para indicar que esta função responderá às solicitações Web para a URL /, que é a URL principal.
#* Jsonify -  is a helper method provided by Flask to properly return JSON data. jsonify() returns a Response object with the application/json mimetype set, whereas json. dumps() simply returns a string of JSON data.
'''

# iremos instanciar o nome do arquivo
app = Flask(__name__)

# rota padrao

from flask import Flask, jsonify, request
@app.route('/')
def obter_postagens():
    return print('Hello')
    # return jsonify(postagens)