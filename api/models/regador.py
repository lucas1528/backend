from models import db

class RegadorModel(db.Model):
    __tablename__ = 'regadores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    funcionamento_geral = db.Column(db.Float(precision=2))
    funcionamento_das_aletas = db.Column(db.Boolean())
    funcionamento_do_motor = db.Column(db.Boolean())
    velocidade_das_aletas = db.Column(db.Integer)
    temporizador = db.Column(db.Integer)

    def __init__(self, nome, funcionamento_geral, funcionamento_das_aletas, funcionamento_do_motor, velocidade_das_aletas, temporizador):
        self.nome = nome
        self.funcionamento_geral = funcionamento_geral
        self.funcionamento_das_aletas = funcionamento_das_aletas
        self.funcionamento_do_motor = funcionamento_do_motor
        self.velocidade_das_aletas = velocidade_das_aletas
        self.temporizador = temporizador
    
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'funcionamento_geral': self.funcionamento_geral,
            'funcionamento_das_aletas': self.funcionamento_das_aletas,
            'funcionamento_do_motor': self.funcionamento_do_motor,
            'velocidade_das_aletas': self.velocidade_das_aletas,
            'temporizador': self.temporizador
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
    
    def update_regador(self, id, nome, funcionamento_geral, funcionamento_das_aletas, funcionamento_do_motor, velocidade_das_aletas, temporizador):
        self.nome = nome
        self.funcionamento_geral = funcionamento_geral
        self.funcionamento_das_aletas = funcionamento_das_aletas
        self.funcionamento_do_motor = funcionamento_do_motor
        self.velocidade_das_aletas = velocidade_das_aletas
        self.temporizador = temporizador

    def delete_regador(self):
        db.session.delete(self)
        db.session.commit()