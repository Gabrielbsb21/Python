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
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:MrRobot0116#@localhost:3306/project_flask' #mysql+mysqldb://user:passwd@host:port/database
    '''
    - Preenca com os dados do seu banco de dados:
    - User -> Usúario do banco
    - Passwd -> Senha do usúario
    - Host -> Geralmente no local fica localhost
    - Port -> Geralmente 3306 no mysql, mas vai depender do banco que você vai usar
    - Databse -> Nome do banco de dados 
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
    IP_HOST = 'localhost'  # geralmente aqui vai um IP do ambiente de teste
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost'  # aqui vai o IP do servidor de produção
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'development': DevelopmentConfig()
}

app_active = os.getenv('FLASK_ENV')
