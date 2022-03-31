from api.resources import planta


def init_api(api):
    api.add_resource(planta.Plantas, '/plantas', endpoint='api/v1')
    api.add_resource(planta.Planta, '/planta', '/planta/<int:id>')
