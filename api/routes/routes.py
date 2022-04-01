from api.resources import planta


def init_api(api):
    api.add_resource(planta.Planta, '/plantas', '/plantas/<int:id>')
