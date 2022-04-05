from api.recursos import irrigador, planta


def inicia_app(api):
    api.add_resource(planta.Planta, '/plantas', '/plantas/<int:id>')
    api.add_resource(irrigador.Irrigador, '/irrigadores', '/irrigadores/<int:id>')
