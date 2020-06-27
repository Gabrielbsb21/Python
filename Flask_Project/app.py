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
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/')
    def index():
        return '<h1>Hello, Jedi!!</h1>'

    @app.route('/login')
    def login():
        return 'Aqui entrará a tela de login'

    @app.route('/recovery-password')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'
    '''
    route de teste
    @app.route('/profile/<string:nome>/<int:idade>/')
    def profile(nome, idade):
        return f'O nome desse usuário é {nome} com idade de {idade}'
    '''

    @app.route('/profile', methods=['POST'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']
        return f'Essa rota possui um método POST e criará um usuário com os dados {username} e {password}'

    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']
        return f'Essa rota possui um método PUT e editará o nome do usuário para {username} e a senha para {password}'
    return app
