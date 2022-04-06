from api.recursos import irrigador, planta, documentacao


def inicia_app(api):
    """Inicia as rotas da api

    Argumento:
        api (classe): Classe Api(Flask(__name__))
    """
    api.add_resource(planta.Planta, '/plantas', '/plantas/<int:id>')
    api.add_resource(irrigador.Irrigador, '/irrigadores', '/irrigadores/<int:id>')
    api.add_resource(documentacao.Documentacao, '/')

