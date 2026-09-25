# 🌐 Estudos sobre Flask

Repositório criado para registrar meus estudos e práticas com **Flask**, um framework web desenvolvido em Python.

O objetivo é explorar gradualmente os principais conceitos utilizados no desenvolvimento de aplicações web e APIs com Flask, utilizando exemplos práticos e comentários no código.

## 📚 Conteúdos estudados

Até o momento, foram abordados os seguintes conceitos:

* Criação e configuração básica de uma aplicação Flask;
* WSGI (Web Server Gateway Interface);
* Criação de rotas;
* Rotas parametrizadas;
* Parâmetros de consulta (Query Parameters);
* Uso do objeto `request`;
* Tratamento de dados utilizando `escape()`;
* Conceitos básicos de prevenção contra XSS;
* Comportamento de URLs com e sem barra final;
* Construção dinâmica de URLs utilizando `url_for()`;
* Métodos HTTP;
* Requisições GET e POST;
* Separação de rotas utilizando `@app.get()` e `@app.post()`;
* Execução da aplicação em modo de desenvolvimento.

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* MarkupSafe
* Git
* GitHub

---

## 📂 Estrutura atual

```text
flask/
│
├── app.py
├── README.md
└── .gitignore
```

O arquivo `app.py` concentra os exemplos e anotações utilizados durante os estudos.

---

## 🚀 Criando uma aplicação Flask

Uma aplicação Flask básica pode ser criada da seguinte maneira:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

`Flask(__name__)` cria uma instância da aplicação.

O decorador `@app.route()` associa uma URL a uma função Python.

---

## 🔗 Rotas

As rotas determinam qual função será executada quando determinada URL for acessada.

Exemplo:

```python
@app.route("/helloWorld")
def hello_world():
    return "<p>Hello, World!</p>"
```

Ao acessar:

```text
http://127.0.0.1:5000/helloWorld
```

o Flask executa a função `hello_world()`.

---

## 🔎 Query Parameters

Parâmetros também podem ser enviados através da URL.

Exemplo:

```python
@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask, Ana")
    return f"Hello, {escape(name)}"
```

Uma requisição pode ser realizada utilizando:

```text
/hello?name=Nicolas
```

Nesse caso, o parâmetro `name` terá o valor `Nicolas`.

---

## 🔐 Escape e XSS

Dados fornecidos pelo usuário não devem ser considerados automaticamente como HTML confiável.

O `escape()` pode ser utilizado para transformar caracteres especiais em representações seguras:

```python
from markupsafe import escape

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"
```

Isso ajuda a impedir que determinados conteúdos fornecidos pelo usuário sejam interpretados como código HTML ou JavaScript, reduzindo riscos de ataques como **Cross-Site Scripting (XSS)**.

---

## 🔀 Rotas parametrizadas

O Flask permite definir partes variáveis dentro das URLs.

### String

```python
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"
```

Exemplo:

```text
/user/Ana
```

### Integer

```python
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"
```

Exemplo:

```text
/post/10
```

### Path

```python
@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"
```

O conversor `path` permite receber valores que também contenham `/`.

---

## 🔗 Construção de URLs com `url_for()`

O Flask disponibiliza `url_for()` para gerar URLs a partir do nome das funções associadas às rotas.

```python
@app.route("/")
def index():
    return "Index"

@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"
```

Exemplo:

```python
url_for("index")
url_for("profile", username="Ana Clara")
```

Essa abordagem evita a necessidade de escrever manualmente as URLs da aplicação.

---

## 📡 Métodos HTTP

Por padrão, uma rota Flask responde ao método HTTP `GET`.

Também é possível permitir outros métodos:

```python
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return "POST"

    return "GET"
```

Alguns dos principais métodos HTTP são:

| Método | Utilização                        |
| ------ | --------------------------------- |
| GET    | Consultar informações             |
| POST   | Enviar ou criar informações       |
| PUT    | Substituir/atualizar um recurso   |
| PATCH  | Atualizar parcialmente um recurso |
| DELETE | Excluir um recurso                |

---

## 📥 `@app.get()` e `@app.post()`

Também é possível separar cada método em uma função diferente.

```python
@app.get("/login")
def login_get():
    return "GET"

@app.post("/login")
def login_post():
    return "POST"
```

Assim:

```text
GET /login
     ↓
login_get()

POST /login
     ↓
login_post()
```

---

## ⚙️ Executando o projeto

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Entre na pasta

```bash
cd flask
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual no Windows

```bash
.venv\Scripts\activate
```

### 5. Instale o Flask

```bash
pip install Flask
```

### 6. Execute a aplicação

```bash
python app.py
```

O servidor de desenvolvimento será iniciado normalmente em:

```text
http://127.0.0.1:5000
```

---

## 📝 Observações

O código deste repositório possui comentários e exemplos voltados para fins de estudo.

Novos conceitos serão adicionados conforme o avanço dos estudos em desenvolvimento Web Back-End com Flask.

## 📖 Próximos estudos

Os próximos conteúdos a serem explorados incluem:

* JSON com Flask;
* Desenvolvimento de Web APIs;
* Manipulação de dados enviados por POST;
* Códigos de status HTTP;
* Tratamento de erros;
* Organização utilizando Models e Controllers;
* Integração com MySQL;
* CRUD;
* Paginação;
* Desenvolvimento de uma API JSON completa.

---

## 👩‍💻 Autora

**Ana Clara de Souza**

Estudante de Sistemas de Informação — UTFPR.
