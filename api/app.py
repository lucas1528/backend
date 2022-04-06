from flask import Flask
from flask_restful import Api

from .api.configuracoes import configuracao_banco_de_dados as config_db
from .api.modelos import banco_de_dados as db
from .api.rotas import rotas

app = Flask(__name__)

@app.before_first_request
def criar_banco_de_dados():
    """cria o banco de dados antes da primeira requisição
    """
    db.create_all()

def criar_app():
    """cria a aplicação da api

    Retorno:
        objeto: Instancia da classe Flask com todas as configurações da aplicação realizadas
    """
    config_db.inicia_app(app)

    api = Api(app)
    rotas.inicia_app(api)

    db.init_app(app)

    return app