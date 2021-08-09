'''Modos de acesso com o arquivos OPEN()
r	Somente leitura
w	Escrita, apagando (truncando) o conteúdo existente no arquivo
a	Escrita, preservando o conteúdo existente (append). O arquivo é criado, se não existir. O texto é inserido no final do arquivo.
b	Modo binário
+	Abre o arquivo para atualização – leitura e escrita
x	Abre o arquivo para criação exclusiva, falhando se o arquivo já existir.
t	Modo de texto (padrão)

>> a função open retorna um objeto manipulador>> arquivo = open(arquivo, modo) 
'''
manipulador = open('arquivo.txt','r')       # a variavel manipulador contém o arquivo.txt
print('\nUtilizando o metodo Read\n')
print(manipulador.read())
                
'''                   
# 1) Criando e lendo arquivos no modo w
arquivo = open('arq01.txt','w')                 #fez o open - faz o close
arquivo.write('Teste de escrita')
arquivo.write('\nBoson Treinamentos')
arquivo.write('\nPor hoje é tudo pessoal.')
arquivo.close()

arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()                      #retorna a string da variavel, removendo espaços.
    print(linha)
arquivo.close()

# 2) Acrescentando no arquivo no modo a

print('\n Digite o texto para incluir no arquivo')
texto = input('Digite uma frase para incluir')
arquivo2 = open('arq01.txt','a')
arquivo2.write(texto + '\n')
print('Operaçao concluida no arquivo' +arquivo2.name)
arquivo2.close()'''