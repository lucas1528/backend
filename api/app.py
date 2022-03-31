from flask import Flask
from flask_restful import Api

from .config import config_db
from .models import db
from .routes import routes


app = Flask(__name__)

@app.before_first_request
def cria_banco():
    db.create_all()

def create_app():
    config_db.init_app(app)

    api = Api(app)
    routes.init_api(api)

    db.init_app(app)

    return app


