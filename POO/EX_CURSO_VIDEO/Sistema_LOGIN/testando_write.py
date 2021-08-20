#escrevendo no arquvio com e sem with

#with open('users_sistema.txt','w') as arquivo:
#    arquivo.write("Testando a escrita malandro2")
   
with open('users_sistema.txt','r') as arquivo:
    print(arquivo.read())