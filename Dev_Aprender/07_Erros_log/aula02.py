import logging

# PROJETO PARA VERIFICAR USUARIO E SENHA

logging.basicConfig(
    level = logging.DEBUG,
    filename= 'aula02.log',
    filemode= 'a',
    datefmt= '%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s- %(message)s'
    )
#output - 2022-09-12 10:29:42 - INFO- victor1cg@hotmail.com logou no sistema;

# email = 'victor1cg@hotmail.com'
# senha = int(input('Coloque sua senha: '))

try :
    email = 'victor1cg@hotmail.com'
    senha = int(input('Coloque sua senha: '))

    if senha == 1234:
        print('\nLOGADO! ')
        logging.info(f'{email} - logou no sistema;')
    else:
        print('\nSenha incorreta!')
        logging.error(f'{email} - senha incorreta: {senha};')

except Exception as erro:
    print('\nErro!')
    logging.error(f'{email} - {erro};')
