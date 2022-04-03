from api.models import db
import datetime



class PlantModel(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    species = db.Column(db.String(40))
    localization = db.Column(db.String(20))
    start_of_cultivation = db.Column(db.Date())

    def __init__(self, name, species, localization, start_of_cultivation):
        self.name = name
        self.species = species
        self.localization = localization
        self.start_of_cultivation = start_of_cultivation
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'localization': self.localization,
            'start_of_cultivation': str(self.start_of_cultivation)
        }
    
    @classmethod
    def find_plant(cls, id):
        plant = cls.query.get(id)
        if plant:
            return plant
        return None

    def save_plant(self):
        db.session.add(self)
        db.session.commit()
    
    def update_plant(self, name, species, localization, start_of_cultivation):
        self.name = name
        self.species = species
        self.localization = localization
        self.start_of_cultivation = start_of_cultivation

    def delete_plant(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def format_date(cls, data):
        date = data['start_of_cultivation'].split('-')
        date = list(map(int, date))
        data['start_of_cultivation'] = datetime.date(date[0],date[1], date[2])
        return data
    
    def not_null(self, data,):
        object = self.json()
        for key, value in data.items():
            if not value:
                data[key] = object[key]
        return data
