from flask import Flask, request, url_for
# WSGI (Web Server Gateway Interface) é um padrão que conecta servidores web a aplicações ou frameworks escritos em Python.
from markupsafe import escape
#utilizado para tratar o conteúdo que vem do usuário de forma segura

app = Flask(__name__) #Instanciando a classe do flask

@app.route("/helloWorld")
def hello_world():
    return "<p> Hello, World!</P>"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask, Ana")
    return f"Hello, {escape(name)}"

#hello?name=Nicolas
#o escape faz os caracteres especiais serem convertidos para entidade HTML,
#qualquer coisa que venha do uu´rio é tratada como dado, não como HTML confiável

#evita ataques XSS (Cross-Site Scripting)

#ROTEAMENTO
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

#REGRAS VARIÁVEIS

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

#URLS únicos / Comportamento de redirecionamento
#As dus regras a seguir diferem no uso da barra final

#parecido com uma pasta (analogia)
@app.route('/projects/') #URL canonica dessa rota (rota principal)
def projects():
    return 'The project page'

#se acessar a url sem a barra no final o flask ira redirecionar para a url com a barra final

#parecido com um arquivo (analogia)
@app.route('/about')
def about():
    return 'The about page'

#se adiiconar uma barra no final ofask ira gerar um erro 404 "não encontrado"

#isso ajuda a manter as URLS exclusivas para esses recurso, o que impedem que os mecanimos de busca
# ndexem a mesm página duas vezes

#--Construção de URLS para funções específicas (url_for())--

#aceita nome d função como primeiro argumento e qualquer qtd de de argumentos nomeados,
#cada um corresponde a uma parte variavel da regra da URL. Partes variaveis desconhecidas são anexaas a URL como parametros de conuslta


@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>') #parte variavel
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/')) #depois que fizer login va para
    print(url_for('profile', username='Ana Clara')) 


#MÉTODOS HTTP

#por padrão responde GET
#com o argumento 'methods' é possivel lidar com dferentes métodos

def do_the_login_form():
    pass

def show_the_login_form():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login_form()
    else:
        return show_the_login_form()

#ex acima mantém todos os métos da rota dentro de uma única função, útil se cda parte usar alguns dads em comum

#Separando as vsualizações para diferentes métodos em funçoes diferentes:

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/lteste')
def login_post():
    return do_the_login_form()


if __name__ == "__main__":
    app.run(debug=True)