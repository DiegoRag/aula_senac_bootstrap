from flask import Flask, render_template, request, url_for
from forms import formLogin, formNovoUsuario

app = Flask(__name__)

app.config['SECRET_KEY'] = '07ced41fe132b166347a6f014a704f51aacfddf919ad41b182562d0668b344f8'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_ead')
def sobre_ead():
    return render_template('sobre_ead.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/login', methods=['get', 'post'])
def login():
    titulo = 'Login de Acesso'
    descricao = 'Formulario formulario de login'

    form_login = formLogin()
    form_novo_usuario = formNovoUsuario()


    return render_template('login.html', titulo=titulo, 
                                         descricao=descricao,
                                         form_login=form_login,
                                         form_novo_usuario=form_novo_usuario)

@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)