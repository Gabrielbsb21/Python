import os
import random
import string


class Config(object):
    CSRF_ENABLED = True
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = '#mysql+mysqldb://user:passwd@host:port/database' #mysql+mysqldb://user:passwd@host:port/database
    '''
    #Informações sobre o Banco de Dados
    # User - Usuário do banco
    # Passwd - Senha do usuário
    # Host - Geralmente no local fica localhost
    # Port - Geralmente 3306 no mysql
    # Database - Nome do Banco de dados
    '''


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'  # Aqui geralmente fica o IP de um servidor
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    TESTING = False
    DEGUB = False
    IP_HOST = 'localhost'  # Aqui vai ficar o IP do servidor de produção
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
