from api.models import db
from datetime import date



class PlantaModel(db.Model):
    __tablename__ = 'plantas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    especie = db.Column(db.String(40))
    localizacao = db.Column(db.String(20))
    inicio_do_cultivo = db.Column(db.Date())

    def __init__(self, nome, especie, localizacao, inicio_do_cultivo):
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.inicio_do_cultivo = inicio_do_cultivo
    
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'especie': self.especie,
            'localizacao': self.localizacao,
            'inicio_do_cultivo': str(self.inicio_do_cultivo)
        }
    
    @classmethod
    def find_planta(cls, id):
        planta = cls.query.get(id)
        if planta:
            return planta
        return None

    def save_planta(self):
        db.session.add(self)
        db.session.commit()
    
    def update_planta(self, nome, especie, localizacao, inicio_do_cultivo):
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.inicio_do_cultivo = inicio_do_cultivo

    def delete_planta(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def format_data(cls, dados):
        data = dados['inicio_do_cultivo'].split('-')
        data = list(map(int, data))
        dados['inicio_do_cultivo'] = date(data[0], data[1], data[2])
        return dados