from api.models import db
from random import randint

class WateringCanModel(db.Model):
    __tablename__ = 'watering_cans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    localization = db.Column(db.String(20))
    timer = db.Column(db.Integer)
    voltage = db.Column(db.Float(precision=2))
    operation = db.Column(db.Boolean())

    def __init__(self, name, localization, timer, voltage, operation):
        self.name = name
        self.localization = localization
        self.timer = timer
        self.voltage = voltage
        self.operation = operation
        
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'localization': self.localization,
            'timer': self.timer,
            'voltage': self.voltage,
            'operation': self.operation
        }
    
    @classmethod
    def find_watering_can(cls, id):
        watering_can = cls.query.get(id)
        if watering_can:
            return watering_can
        return None

    def save_watering_can(self):
        db.session.add(self)
        db.session.commit()
    
    def update_watering_can(self, name, localization, timer, voltage, operation):
        self.name = name
        self.localization = localization
        self.timer = timer
        self.voltage = voltage
        self.operation = operation
        

    def delete_watering_can(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def simulate_watering_can(cls):
        simulation = dict()
        if randint(0, 100) % 2 == 0:
            simulation['operation'] = True
        else:
            simulation['operation'] = False

        if randint(0, 100) % 2 == 0:
            simulation['voltage'] = randint(110, 120)
        else:
            simulation['voltage'] = randint(75, 90)

        return simulation
    
    def format_data(self, data):
        object = self.json()
        for key, value in data.items():
            if not value:
                data[key] = object[key]
        return data