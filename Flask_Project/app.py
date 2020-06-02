# -*- coding: utf-8 -*-
from flask import Flask
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask import request

config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLACHEMY_DATABASE_URI'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello, Jedi'
    
    @app.route('/login/')
    def login():
        return 'Aqui vai ter uma tela de login'
    
    @app.route('/recovery-password/')
    def recovery_password():
        return 'Tela para recuperação de senha'
    
    @app.route('/profile/<int:id>/action/<action>')
    def profile(id, action):
        return f'Ação {action} usuário de ID {id}' # f'string do Python
    
    @app.route('/profile/', methods=['POST']) # Enviar dados ao servidor
    def create_profile():
        username = request.form['username']
        password = request.form['password']

        return f'Essa rota possui um método POST e criará um usuário com os dados de usuários {username} e senha {password}'
    
    @app.route('/profile/<int:id>', methods=['PUT']) # Atualizar um dado no servidor
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']

        return f'Essa rota possui um método PUT e editará o nome do usuário para {username} e a senha para {password}'


    return app
