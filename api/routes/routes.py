from api.resources import planta, regador


def init_api(api):
    api.add_resource(planta.Planta, '/plantas', '/plantas/<int:id>')
    api.add_resource(regador.Regador, '/regadores', '/regadores/<int:id>')
