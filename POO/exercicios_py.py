# Exercicio criando um sistema da Netflix

class Cliente:
    def __init__(self,nome,email,plano):
        self.nome = nome                        #Atributos
        self.email = email
        self.plano = plano
        self.planos = ['basico','premium']
        
        if plano in self.planos:
            self.plano = plano
            print(f'\nO plano é {plano}')
        else:
            raise Exception('\nPlano inválido!') #Caso o plano não esteja na lista


    def mudar_plano(self,novo_plano):           #funçoes
        if novo_plano in self.planos:           #como atribui o self.planos, consigo utilizar dentro da classe
            self.plano = novo_plano
        else:
            print('Plano inválido')

    def ver_filme(self,filme,plano_filme):      #caso o filme seja para diferentes planos.Premium roda todos os filmes.
        if self.plano == plano_filme:
            print(f'\nPlay filme {filme}')
        elif self.plano == 'premium':
            print(f'\nPlay filme {filme}')
        elif self.plano == 'basico' and plano_filme == 'premium':
            print('\nRealizar upgrade para Premium!\n')
        else:
            print('\nPlano invalido!')


### Importante. Uma variavel recebe a classe, e portanto usamos as funções e atributo 
cliente = Cliente('Victor','victor@gmail.com','premium')
#print(cliente.plano)                           #printar os atributos

cliente.ver_filme('Top Gun','basico')


