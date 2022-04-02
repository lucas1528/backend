from api.models import db
from random import randint

class RegadorModel(db.Model):
    __tablename__ = 'regadores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    localizacao = db.Column(db.String(20))
    temporizador = db.Column(db.Integer)
    voltagem_do_regador = db.Column(db.Float(precision=2))
    funcionamento_do_regador = db.Column(db.Boolean())

    def __init__(self, nome, localizacao, temporizador, voltagem_do_regador, funcionamento_do_regador):
        self.nome = nome
        self.localizacao = localizacao
        self.temporizador = temporizador
        self.voltagem_do_regador = voltagem_do_regador
        self.funcionamento_do_regador = funcionamento_do_regador
        
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'localizacao': self.localizacao,
            'temporizador': self.temporizador,
            'voltagem_do_regador': self.voltagem_do_regador,
            'funcionamento_do_regador': self.funcionamento_do_regador
        }
    
    @classmethod
    def find_regador(cls, id):
        regador = cls.query.get(id)
        if regador:
            return regador
        return None

    def save_regador(self):
        db.session.add(self)
        db.session.commit()
    
    def update_regador(self, nome, localizacao, temporizador, voltagem_do_regador, funcionamento_do_regador):
        self.nome = nome
        self.localizacao = localizacao
        self.temporizador = temporizador
        self.voltagem_do_regador = voltagem_do_regador
        self.funcionamento_do_regador = funcionamento_do_regador
        

    def delete_regador(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def simula_funcionamento(cls):
        simulacao = dict()
        if randint(0, 100) % 2 == 0:
            simulacao['funcionamento_do_regador'] = True
        else:
            simulacao['funcionamento_do_regador'] = False

        if randint(0, 100) % 2 == 0:
            simulacao['voltagem_do_regador'] = randint(110, 120)
        else:
            simulacao['voltagem_do_regador'] = randint(75, 90)

        return simulacao
    
    def format_data(self, dados):
        objeto = self.json()
        for key, value in dados.items():
            if not value:
                dados[key] = objeto[key]
        return dados