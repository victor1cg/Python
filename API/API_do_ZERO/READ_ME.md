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
## Estrutura de pastas e arquivos
Script para criar os arquivos do projeto.
```
# Arquivos na raiz
touch setup.py
touch {settings,.secrets}.toml
touch {requirements,MANIFEST}.in
touch Dockerfile.dev docker-compose.yaml

# Imagem do banco de dados
mkdir postgres
touch postgres/{Dockerfile,create-databases.sh}

# Aplicação
mkdir -p pamps/{models,routes}
touch pamps/default.toml
touch pamps/{__init__,cli,app,auth,db,security,config}.py
touch pamps/models/{__init__,post,user}.py
touch pamps/routes/{__init__,auth,post,user}.py

# Testes
touch test.sh
mkdir tests
touch tests/{__init__,conftest,test_api}.py
```
Esta será a estrutura final (se preferir criar manualmente)

```
❯ tree -a -I docs -I .git
.
├── docker-compose.yaml        # Orquestração de containers
├── Dockerfile.dev             # Imagem principal
├── MANIFEST.in                # Arquivos incluidos na aplicação
├── requirements-dev.txt       # Dependencias de ambiente dev
├── requirements.in            # Dependencias de produção
├── .secrets.toml              # Senhas locais
├── settings.toml              # Configurações locais
├── setup.py                   # Instalação do projeto
├── test.sh                    # Pipeline de CI em ambiente dev
├── pamps
│   ├── __init__.py
│   ├── app.py                 # FastAPI app
│   ├── auth.py                # Autenticação via token
│   ├── cli.py                 # Aplicação CLI `$ pamps adduser` etc
│   ├── config.py              # Inicialização da config
│   ├── db.py                  # Conexão com o banco de dados
│   ├── default.toml           # Config default
│   ├── security.py            # Password Validation
│   ├── models
│   │   ├── __init__.py
│   │   ├── post.py            # ORM e Serializers de posts
│   │   └── user.py            # ORM e Serialziers de users
│   └── routes
│       ├── __init__.py
│       ├── auth.py            # Rotas de autenticação via JWT
│       ├── post.py            # CRUD de posts e likes
│       └── user.py            # CRUD de user e follows
├── postgres
│   ├── create-databases.sh    # Script de criação do DB
│   └── Dockerfile             # Imagem do SGBD
└── tests
    ├── conftest.py            # Config do Pytest
    ├── __init__.py
    └── test_api.py            # Tests da API