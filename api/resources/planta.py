from flask_restful import Resource, reqparse
from api.models.planta import PlantaModel


class Planta(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    args.add_argument('especie', type=str, required=True, help="The field 'especie' cannot be left blank.")
    args.add_argument('localizacao', type=str, required=True, help="The field 'localizacao' cannot be left blank.")
    args.add_argument('inicio_do_cultivo', required=True, help="The field 'inicio_do_cultivo' cannot be left blank.")

    def get(self, id=None):
        if id:
            planta = PlantaModel.find_planta(id)
            if planta:
                return planta.json()
            return {'message': 'Planta not found.'}, 404
        plantas = {
            'plantas': [planta.json() for planta in PlantaModel.query.all()]
        }
        return plantas
    
    def post(self):
        dados = Planta.args.parse_args()
        dados = PlantaModel.format_data(dados)
        planta = PlantaModel(**dados)
        try:
            planta.save_planta()
        except:
            return {'message': 'An internal error ocurred trying to save planta.'}, 500
        return planta.json()

    def patch(self, id):
        planta = PlantaModel.find_planta(id)
        if planta:
            dados = Planta.args.parse_args()
            dados = PlantaModel.format_data(dados)
            planta.update_planta(**dados)
            try:
                planta.save_planta()
            except:
                return {'message': 'An internal error ocurred trying to update hotel.'}, 500
            return planta.json(), 200
        return {'message': 'Planta not found.'}, 404
            
    def delete(self, id):
        planta = PlantaModel.find_planta(id)
        if planta:
            try:
                planta.delete_planta()
            except:
                return {'message': 'An internal error ocurred trying to delete hotel.'}, 500
            return {'message': 'Planta deleted.'}, 200
        return {'message': 'Planta not found.'}, 404