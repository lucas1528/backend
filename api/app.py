from flask import Flask
from flask_restful import Api

from .configuracoes import configuracao_banco_de_dados as config_db
from .modelos import banco_de_dados as db
from .rotas import rotas

app = Flask(__name__)

@app.before_first_request
def criar_banco_de_dados():
    db.create_all()

def criar_app():
    config_db.inicia_app(app)

    api = Api(app)
    rotas.inicia_app(api)

    db.init_app(app)

    return app