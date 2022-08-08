
#! Criando nossa primeira API

# Frameworks mais utilizados - Flask e Django

from flask import Flask, jsonify, request

# *Flask - object que criará uma função que retorna uma resposta HTTP - Criar um webserver em menos de 7 linhas
''' 
@app.route é um decorador que transforma uma função Python comum em uma função de visualização Flask. Ela converte o valor de retorno da função em uma resposta HTTP para ser mostrada por um cliente HTTP, como um navegador Web. Passe o valor '/' para @app.route() para indicar que esta função responderá às solicitações Web para a URL /, que é a URL principal.
#* Jsonify -  is a helper method provided by Flask to properly return JSON data. jsonify() returns a Response object with the application/json mimetype set, whereas json. dumps() simply returns a string of JSON data.
'''
#! Aula 08 API - 
# iremos instanciar o nome do arquivo
app = Flask(__name__)

from flask import Flask, jsonify, request

#basico de montar servidor
""" @app.route('/')             # function for a given URL rule
def obter_postagens():
    return print('Hello')
    # return jsonify(postagens) """

#Criando uma API para oferecer consultas ao arquivo postagens
postagens = [
    {
        'titulo':'Minha historia',
        'autor':'Amanda Dias'
    },
    {
        'titulo':'Novo dispositivo Sony',
        'autor':'Howard Stringer'
    },
    {
        'titulo':'Lancamento do Ano',
        'autor':'Jeff Bezos'
    }
]   

print(postagens[0]['titulo'])

# Rota Padrao - GET - http://localhost:5000/
@app.route('/')
def obter_postagens():
    return jsonify(postagens)   #Dumps - Ele transforma a saída JSON em um objeto ~flask.

if __name__ == '__main__':
    app.run(port=5000, host= 'localhost', debug=True)

# Obtendo um dado especifico - segunda postagem 
