
#! APIs
# Uma API é um conjunto de rotinas, protocolos e ferramentas para construir aplicações.

#* Toda API possui 4 partes:
# URL Base - https://api.spotify.com/ - É a url base para consulta
# Endpoint - https://api.spotify.com/artist - Artist é o endpoint, onde seu serviço pode ser acessado por uma aplicação cliente.
# Recurso - Tudo que é enviado ou recebido.
# Verbos HTTP -
''' GET- Obter dados existentes;
    POST- Enviar dados;
    PUT- Atualizar dados;
    DELETE- Excluir dados;
'''  
# Status Code 
''' 1XXX - Informaçao
    2XXX - Sucesso
    3XXX - Redirecionamento
    4XXX - Cliente (403 erro na pagina. F12 na web > Network > Status do objetos)
    5XXX - Servidor
'''

#! Consultando e Utilizando
# 1) pip install requests

import requests
from pprint import pprint

#*GET - Obter dados
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#*GET c/ ID , selecionar o id = 2
resultado_get_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_id.json())

#*POST - Criar nova informação
tarefa = {'completed': False,
            'title': 'Finalizar o curso python',
            'userId': 1}

#necessario criar no mesmo formato. ID é gerado automaticamente            
resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos',tarefa)
#pprint(resultado_post.json())

#* PUT - Alterar um recurso existente
tarefa_alterada = {'completed': False,
                    'title': 'Finalizar o curso SPARK',
                    'userId': 1}

resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2',tarefa_alterada)

#pprint(resultado_put.json())
#pprint(resultado_get_id.json())

#* DELETE - deletar um recurso
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())
# ira retornar um {} vazio. OK!