from api.modelos import banco_de_dados as db
from datetime import date



class ModeloPlanta(db.Model):
    __tablenome__ = 'plantas'

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
    
    def atualizar_planta(self, nome, especie, localizacao, inicio_do_cultivo):
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.inicio_do_cultivo = inicio_do_cultivo
    
    @classmethod
    def formatar_data(cls, dados):
        data = dados['inicio_do_cultivo'].split('-')
        data = list(map(int, data))
        dados['inicio_do_cultivo'] = date(data[0],data[1], data[2])
        return dados
