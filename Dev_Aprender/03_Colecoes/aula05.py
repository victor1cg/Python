
#! SETS - Conjuntos {}
# São mutaveis, podemos adicionar elementos, POREM possui valores unicos.
# Sort os elementos.
from pathlib import Path
import json
import pprint

frutas = {'maca', 'banana', 'banana', 'uva'}
# print(set(frutas))

# Conjuntos
num1 = {1, 2, 4, 5, 7}
num2 = set([2, 5, 6, 1])
# print(num1.symmetric_difference(num2)) #Diferença de conjuntos
# print(num1.intersection(num2))
# print(num1.union(num2))

#! JSON - Java Script Object Notation
# Muito usado em APIs, para enviar info. Arquivo leve, e estrutura organizada em chave valor.
# * Object >> json.dump(Encode) >> File(Json formatted)
# * File(Json formatted) >> json.load(Decode) >> Object


carros = [
    {'marca': 'Nissan', 'Preco': 18000, 'Cor': 'Prata'},
    {'marca': 'Audi', 'Preco': 11000, 'Cor': 'Prata'},
    {'marca': 'Volks', 'Preco': 15000, 'Cor': 'Vermelho'},
    {'marca': 'Volks', 'Preco': 15000, 'Cor': 'Azul'}
]

# salvando arquivo
""" carros_json = json.dumps(carros)  # encode
Path(r'Dev_Aprender/03_Colecoes/carros.json')\
    .write_text(carros_json)   """

# lendo o arquivo
""" arquivo_carros_json = Path(r'Dev_Aprender/03_Colecoes/carros.json')\
                                    .read_text() #carrega o arquivo puro, Open the file in text mode, read it, and close the file.
arquivo_json = json.loads(arquivo_carros_json)   #transforma em json
print('\n' + arquivo_json[0]['marca'] + '- Acessando a marca do carro.') """

#todo - DESAFIO - Encontrar e exibir na tela a 'ability' 'lightning -rod', do arquivo pikachu.json

pikachu = Path(r'Dev_Aprender/03_Colecoes/pikachu.json').read_text()
pikachu_json = json.loads(pikachu)

""" print()
pprint.pprint(pikachu_json['abilities'])       """      #printa um json pretty

print()
pprint.pprint(pikachu_json['abilities'][1]['ability']['name'])            #printa um json pretty
#entra no parametro abilities > Escolho a segunda opção > Entra no parametro > escolhe o valor
