
#! Utilizando TRY CATCH - TRATAMENTO de ERROS

""" try:
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(meses[14])
except IndexError as erro:
    print('\nDigite um valor válido !')
    print(erro)                             #conseguimos verificar o erro
 """

#! 02 - Caso precise tomar ação. FINALLY SEMPRE IRA RODAR
# Não ira printar pois internet precisa ser str

""" internet = None
try:
    print("Conectando a " + internet)
except TypeError as erro:
    print("Não foi possível conectar.")
else:                                   #Retorna caso nenhuma erro apareça
    print('Tudo OK')
finally:                                #Sempre retorna
    print("Desfazendo a compra")
 """
#! 03 - CLASS EXCEPTION - acessando as variaveis do erro
""" internet = None
try:
    print("Conectando a " + internet)
except Exception as erro:
    print ('Ocorreu um erro de : {}'.format(erro.__class__))
    print ('Ocorreu um erro de : {}'.format(erro.args))
 """
#! 03 - Utilizando LOGGING para registro.
import logging
'''Níveis de logging (gravidade):
debug | info | warning | error | critical
Por padrão somente log de warning acima é exibido.
Podemos alterar isso no config.
'''
#Setar o nível de exibição, e criar o arquivo para guardar o log.
logging.basicConfig(
    level=logging.DEBUG, 
    filename='app.log',
    filemode='a',
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s- %(message)s')      #format é o modelo que queremos de log, são palavras reservadas;

x = 2                                                       #somente irá guardar o log quando acessar as funções

try:
    logging.debug('logging no nivel')
    logging.info('logging no nivel \n')
    print(10/x)
except:
    logging.warning('logging no nivel')
    logging.error('logging no nivel \n')
finally:
    logging.critical('logging no nivel')