from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed

class formLogin(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    senha = PasswordField('senha', validators=[DataRequired(),Length(6,12)])
    submitLogin = SubmitField('Login')


class formNovoUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    telefone = StringField('Telefone', validators=[])
    documento = StringField('documento', validators=[])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,12)])
    senhaConfirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(),EqualTo('senha')])
    submitCadastro = SubmitField('Criar conta')

class formCadastroProduto(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    descricao = StringField('descricao', validators=[DataRequired()])
    imagem = FileField('imagem', validators=[FileRequired('Informe uma imagem por gentileza')])
    submit = SubmitField('Cadastro Produto')