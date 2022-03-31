from api.models import db


class PlantaModel(db.Model):
    __tablename__ = 'plantas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    especie = db.Column(db.String(80))
    localizacao = db.Column(db.String(80))
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