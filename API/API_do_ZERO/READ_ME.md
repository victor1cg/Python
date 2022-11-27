## GITPOD

 - Ambiente de desenvolvimento em nuvem Linux, com interface de VSCODE que roda em browser. Não é necessario instalar docker, imagens ou ambiente virtual (VENV).  
 - Alem de compartilhar o script com o time, inclui todo o ambiente. Evitando assim, problemas de versão de biblioteca, atualizações e etc.  
 - Ao criar um workspace, é criado um **container com VSCODE** instalado que roda em Linux.
 ---
## CRIANDO UMA API DO ZERO
  
Curso de python backend criando, executando e testando um API com FastAPI. Criaremos um *Blog* simples.

----

*Venv* serve para ambiente de DEV. Para a produção jogamos dentro do container com os pacotes. 

Primeira coisa é atualizar o pip.  
Em seguida instalar o requirements.
```
pip install --upgrade pip
pip install -r requirements-dev.txt
```
---