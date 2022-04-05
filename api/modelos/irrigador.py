from api.modelos import banco_de_dados as db
from random import randint

class ModeloIrrigador(db.Model):
    __tablenome__ = 'irrigadores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    localizacao = db.Column(db.String(20))
    temporizador = db.Column(db.Integer)
    duracao_da_irrigacao = db.Column(db.Integer)
    voltagem = db.Column(db.Float(precision=2))
    irrigando = db.Column(db.Boolean())

    def __init__(self, nome, localizacao, temporizador, duracao_da_irrigacao, voltagem, irrigando):
        self.nome = nome
        self.localizacao = localizacao
        self.temporizador = temporizador
        self.duracao_da_irrigacao = duracao_da_irrigacao
        self.voltagem = voltagem
        self.irrigando = irrigando
        
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'localizacao': self.localizacao,
            'temporizador': self.temporizador,
            'duracao_da_irrigacao': self.duracao_da_irrigacao,
            'voltagem': self.voltagem,
            'irrigando': self.irrigando
        }
    
    def atualizar_irrigador(self, nome, localizacao, temporizador, duracao_da_irrigacao, voltagem, irrigando):
        self.nome = nome
        self.localizacao = localizacao
        self.temporizador = temporizador
        self.duracao_da_irrigacao = duracao_da_irrigacao
        self.voltagem = voltagem
        self.irrigando = irrigando

    @classmethod
    def simular_irrigador(cls):
        simulacao = dict()
        if randint(0, 100) % 2 == 0:
            simulacao['irrigando'] = True
        else:
            simulacao['irrigando'] = False

        if randint(0, 100) % 2 == 0:
            simulacao['voltagem'] = randint(110, 120)
        else:
            simulacao['voltagem'] = randint(75, 90)

        return simulacao
    
    @classmethod
    def verificar_argumentos(cls, dados):
        if dados['nome']:    
            if dados['temporizador']:
                if dados['duracao_da_irrigacao']:
                    return True
        return False