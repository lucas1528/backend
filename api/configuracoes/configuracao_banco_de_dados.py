import os


def inicia_app(app):
    """Inicia as configurações de banco de dados da aplicação.

    Argumentos:
        app (objeto): Instancia da classe Flask da biblioteca flask

    Retornos:
        app: app com alterações nas configurações do banco de dados
    """
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app