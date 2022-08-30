## Nossa Estrutura para CRUD com API e SQLite

1. Classe que representa uma postagem no nosso blog (DB)
2. Classe que representa um autor no nosso blog (DB)
3. API para criar novas postagens (app)
4. API para criar novos autores (app)
    5. Add o banco de dados para cada chamado de Postagem e Autor
    6. Add autenticação a nossas APIs;

postagens = [
    {
        "titulo":"Minha historia",
        "autor":"Amanda Dias"
    },
    {
        "titulo":"Novo dispositivo Sony",
        "autor":"Howard Stringer"
    },
    {
        "titulo":"Lancamento do Ano",
        "autor":"Jeff Bezos"
    }
]  