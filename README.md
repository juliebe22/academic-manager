# Academic Manager 🎓

Sistema de Gerenciamento Acadêmico desenvolvido em Python, integrado ao MongoDB Atlas, com interface gráfica para gerenciamento de alunos.

## Objetivo

O projeto tem como objetivo facilitar o gerenciamento de informações acadêmicas, permitindo cadastrar, consultar, atualizar, excluir e pesquisar registros de alunos.

## Funcionalidades

- Cadastro de alunos.
- Consulta de alunos cadastrados.
- Atualização de informações.
- Exclusão de registros.
- Pesquisa por nome, matrícula e curso.
- Validação de dados.
- Identificação de matrículas duplicadas.

## Tecnologias utilizadas

- Python
- MongoDB Atlas
- PyMongo
- Tkinter
- Python-dotenv
- Git e GitHub

## Estrutura do projeto

```text
academic-manager/
├── main.py
├── database.py
├── alunos.py
├── interface.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/juliebe22/academic-manager.git
```

### 2. Entrar na pasta

```bash
cd academic-manager
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

```bash
venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar o MongoDB Atlas

Crie um arquivo `.env` na raiz do projeto e adicione sua string de conexão:

```env
MONGODB_URI=sua_string_de_conexao
```

### 7. Executar o sistema

```bash
python main.py
```

## Integração com MongoDB Atlas

A aplicação utiliza o MongoDB Atlas para armazenar os dados dos alunos em uma coleção chamada `alunos`, dentro do banco de dados `academic_manager`.

A comunicação entre Python e MongoDB é realizada por meio da biblioteca PyMongo.

## Operações CRUD

O sistema implementa as quatro operações fundamentais:

- **Create:** cadastro de alunos utilizando `insert_one()`.
- **Read:** consulta de registros utilizando `find()`.
- **Update:** atualização de informações utilizando `update_one()`.
- **Delete:** exclusão de registros utilizando `delete_one()`.

Também são utilizadas consultas com filtros para pesquisar alunos por nome, matrícula e curso.

## Autora

Desenvolvido por Júlia Beatriz Borges Cavalcante.

Projeto acadêmico desenvolvido para praticar integração entre Python e MongoDB Atlas.