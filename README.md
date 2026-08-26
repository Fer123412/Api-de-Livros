# 📚 API de Gerenciamento de Livros

Uma API REST simples desenvolvida com **Python** e **Flask** para realizar o gerenciamento de livros. A aplicação permite consultar, cadastrar, editar e excluir livros por meio de requisições HTTP.

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de **APIs REST**, **endpoints**, **métodos HTTP** e manipulação de dados utilizando Flask.

---

## 🚀 Tecnologias utilizadas

* Python
* Flask
* API REST
* JSON

---

## ⚙️ Funcionalidades

A API possui as seguintes operações:

* 📖 Consultar todos os livros
* 🔍 Consultar um livro pelo ID
* ➕ Cadastrar um novo livro
* ✏️ Editar informações de um livro
* 🗑️ Excluir um livro

---

## 📌 Endpoints da API

### 📖 Consultar todos os livros

**Método:** `GET`

```http
/livros
```

**Exemplo de resposta:**

```json
[
    {
        "id": 1,
        "titulo": "game of thrones",
        "autor": "george r. r. martin"
    },
    {
        "id": 2,
        "titulo": "o senhor dos aneis",
        "autor": "j. r. r. tolkien"
    }
]
```

---

### 🔍 Consultar livro por ID

**Método:** `GET`

```http
/livros/<id>
```

**Exemplo:**

```http
/livros/1
```

---

### ➕ Cadastrar um novo livro

**Método:** `POST`

```http
/livros
```

**Exemplo de JSON enviado:**

```json
{
    "id": 4,
    "titulo": "Nome do Livro",
    "autor": "Nome do Autor"
}
```

---

### ✏️ Editar um livro

**Método:** `PUT`

```http
/livros/<id>
```

**Exemplo:**

```http
/livros/1
```

**Dados enviados:**

```json
{
    "titulo": "Novo título",
    "autor": "Novo autor"
}
```

---

### 🗑️ Excluir um livro

**Método:** `DELETE`

```http
/livros/<id>
```

**Exemplo:**

```http
/livros/1
```

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
```

### 2. Acesse a pasta do projeto

```bash
cd nome-do-repositorio
```

### 3. Instale o Flask

```bash
pip install flask
```

### 4. Execute a aplicação

```bash
python api.py
```

A API será executada localmente na porta `5000`.

---

## 🌐 Endereço da API

Após iniciar o servidor, você poderá acessar a API em:

```http
http://localhost:5000/livros
```

---

## 🧪 Testando a API

Você pode testar os endpoints utilizando ferramentas como:

* Postman
* Insomnia
* Thunder Client
* cURL

---

## 🗂️ Estrutura dos dados

Cada livro é representado por um objeto JSON contendo:

| Campo    | Tipo    | Descrição                    |
| -------- | ------- | ---------------------------- |
| `id`     | Integer | Identificador único do livro |
| `titulo` | String  | Título do livro              |
| `autor`  | String  | Nome do autor                |

---

## ⚠️ Observações

Atualmente, os livros são armazenados em uma lista diretamente no código. Portanto, ao reiniciar a aplicação, todas as alterações realizadas durante a execução serão perdidas.

Como melhorias futuras, é possível implementar:

* Integração com banco de dados
* Validação dos dados enviados
* Tratamento de erros
* Retorno de códigos HTTP adequados
* Documentação interativa com Swagger/OpenAPI
* Autenticação de usuários

---

## 👨‍💻 Autor

Desenvolvido por **Fernando**.

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório!
