from flask_restful import Resource, reqparse
from api.models.plant import PlantModel


class Plant(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    args.add_argument('species', type=str, help="The field 'species' is a string.")
    args.add_argument('localization', type=str, help="The field 'localization' is a string.")
    args.add_argument('start_of_cultivation', type=str, help="The field 'start_of_cultivation' is a string in format -> YYYY-mm-dd.")

    def get(self, id=None):
        if id:
            plant = PlantModel.find_plant(id)
            if plant:
                return plant.json()
            return {'message': 'Plant not found.'}, 404
        plants = {
            'plants': [plant.json() for plant in PlantModel.query.all()]
        }
        return plants
    
    def post(self):
        data = Plant.args.parse_args()
        data = PlantModel.format_date(data)
        plant = PlantModel(**data)
        try:
            plant.save_plant()
        except:
            return {'message': 'An internal error ocurred trying to save plant.'}, 500
        return plant.json()

    def patch(self, id):
        plant = PlantModel.find_plant(id)
        if plant:
            data = Plant.args.parse_args()
            data = plant.not_null(data)
            data = PlantModel.format_date(data)
            plant.update_plant(**data)
            try:
                plant.save_plant()
            except:
                return {'message': 'An internal error ocurred trying to update plant.'}, 500
            return plant.json(), 200
        return {'message': 'Plant not found.'}, 404
            
    def delete(self, id):
        plant = PlantModel.find_plant(id)
        if plant:
            try:
                plant.delete_plant()
            except:
                return {'message': 'An internal error ocurred trying to delete plant.'}, 500
            return {'message': 'Plant deleted.'}, 200
        return {'message': 'Plant not found.'}, 404