from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_ead')
def sobre_ead():
    return render_template('sobre_ead.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)