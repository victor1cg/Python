
#! Consumir API com Autenticação utilizando o modulo REQUESTS 
#! Abrir em um novo Terminal. Ou seja, um rodando o localhost e outro com o script

from requests.auth import HTTPBasicAuth
import requests 

#realizando o login para obter o token
token = requests.get('http://localhost:5000/login',auth= ('jow','1234'))
print(token.json())

#utilizando o token para outros endpoints
resultado_autores = requests.get('http://localhost:5000/autores', 
                        headers = {'x-access-token': token.json()['token']})