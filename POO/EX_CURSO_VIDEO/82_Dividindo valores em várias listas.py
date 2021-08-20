#082 - Dividindo valores em várias listas

galera = list()
dado = list()
for c in range(2):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    dado.append(nome)                   #criando a lista dado
    dado.append(idade)                  
    galera.append(dado[:])              # MUITO IMPORTANTE [:],isso cria a conexão da lista dentro da lista
    dado.clear()
    
for p in galera:                        #para cada p na lista galera p[0] p[1], p[0] p[1],...
    if p[1] >= 21:
        print(f"\nO {p[0]} é maior de idade.")
    
            
    
print(galera[0])
    