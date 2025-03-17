# Database CRUD com SQLAlchemy

Este projeto é uma implementação de um CRUD (Create, Read, Update, Delete) utilizando Python e SQLAlchemy para gerenciar um banco de dados relacional. Além disso, há um WebApp simples utilizando Streamlit para autenticação de usuários.

## Tecnologias Utilizadas

- Python  
- SQLAlchemy  
- SQLite (pode ser adaptado para outros bancos de dados)  
- Werkzeug Security (para hash de senhas)  
- Streamlit (para interface web)  

## Funcionalidades

- Criar usuários com senha protegida por hash  
- Ler todos os usuários armazenados no banco de dados  
- Ler um usuário específico por ID  
- Atualizar informações de um usuário  
- Excluir usuários  
- WebApp para login de usuários  

## Instalação e Execução

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

### Clonando o repositório
```bash
  git clone https://github.com/brunabbelini/database-crud-sqlalchemy.git
  cd database-crud-sqlalchemy
```

### Instalando as dependências

```bash
  pip install -r requirements.txt
```

### Executando o CRUD

```bash
  python crud.py
```

### Executando o WebApp

```bash
  streamlit run webapp.py
```

## Estrutura do Projeto
```
 database-crud-sqlalchemy/
 │── crud.py     # Implementação das operações CRUD com SQLAlchemy
 │── webapp.py   # Interface web para login de usuários com Streamlit
 │── requirements.txt  # Dependências do projeto
 │── bd_usuarios.sqlite  # Banco de dados SQLite gerado automaticamente

```

## Descrição dos Arquivos

### `crud.py`

O arquivo `crud.py` contém a implementação do CRUD para a tabela `usuarios`. Ele inclui:

- Definição do modelo de usuário utilizando SQLAlchemy.
- Funções para criar, ler, atualizar e excluir usuários.
- Uso da biblioteca `werkzeug.security` para proteger senhas.

### `webapp.py`

O arquivo `webapp.py` implementa uma interface de login utilizando Streamlit:

- Lista os usuários cadastrados no banco de dados.
- Permite que o usuário selecione seu nome e insira sua senha.
- Valida a senha e exibe mensagens de sucesso ou erro.
- Mantém o estado de login utilizando `st.session_state`.

### Exemplo de Uso

```python
from crud import cria_usuarios, le_todos_usuarios

# Criando um usuário
dados_usuario = {
    "nome": "Bruna Belini",
    "senha": "minha_senha",
    "email": "bruna@email.com",
    "acesso_gestor": True
}
cria_usuarios(**dados_usuario)

# Lendo todos os usuários
usuarios = le_todos_usuarios()
for usuario in usuarios:
    print(usuario)
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Para isso:

1. Faça um fork do repositório
2. Crie uma branch para sua funcionalidade (`git checkout -b minha-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Envie para o repositório remoto (`git push origin minha-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

