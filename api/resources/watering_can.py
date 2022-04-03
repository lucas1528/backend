from flask_restful import Resource, reqparse
from api.models.watering_can import WateringCanModel


class WateringCan(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    args.add_argument('localization', type=str, help="The field 'localization'  is a string.")
    args.add_argument('timer', type=int, help="The field 'timer' is a integer.")

    def get(self, id=None):
        if id:
            watering_can = WateringCanModel.find_watering_can(id)
            if watering_can:
                return watering_can.json()
            return {'message': 'Watering can not found.'}, 404
        all_watering_cans = {
            'watering_cans': [watering_can.json() for watering_can in WateringCanModel.query.all()]
        }
        return all_watering_cans
    
    def post(self):
        data = WateringCan.args.parse_args()
        simulation = WateringCanModel.simulate_watering_can()
        watering_can = WateringCanModel(**data, **simulation)
        try:
            watering_can.save_regador()
        except:
            return {'message': 'An internal error ocurred trying to save watering can.'}, 500
        return watering_can.json()

    def patch(self, id):
        watering_can = WateringCanModel.find_watering_can(id)
        if watering_can:
            data = WateringCan.args.parse_args()
            formatted_data = watering_can.format_data(data)
            simulation = WateringCanModel.simulate_watering_can()
            watering_can.update_watering_can(**formatted_data, **simulation)
            try:
                watering_can.save_watering_can()
            except:
                return {'message': 'An internal error ocurred trying to update watering can.'}, 500
            return watering_can.json(), 200
        return {'message': 'Watering can not found.'}, 404
            
    def delete(self, id):
        watering_can = WateringCanModel.find_watering_can(id)
        if watering_can:
            try:
                watering_can.delete_watering_can()
            except:
                return {'message': 'An internal error ocurred trying to delete watering can.'}, 500
            return {'message': 'Watering can deleted.'}, 200
        return {'message': 'Watering can not found.'}, 404