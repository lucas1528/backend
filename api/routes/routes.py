from api.resources import plant, watering_can


def init_api(api):
    api.add_resource(plant.Plant, '/plants', '/plants/<int:id>')
    api.add_resource(watering_can.WateringCan, '/watering_cans', '/watering_cans/<int:id>')
