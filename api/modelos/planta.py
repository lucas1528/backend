from api.modelos import banco_de_dados as db
from datetime import date



class ModeloPlanta(db.Model):
    """Classe modelo que herda modelo base da ORM (SQLAlchemy), Utilizada para
    instanciar objetos a serem criados, deletados, atualizados e obtidos através
    de metodos http e querys da ORM

    Argumentos:
        db.Model (classe): Classe modelo base da ORM (SQLAlchemy)
    """
    __tablenome__ = 'plantas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    especie = db.Column(db.String(40))
    localizacao = db.Column(db.String(20))
    inicio_do_cultivo = db.Column(db.Date())

    def __init__(self, nome, especie, localizacao, inicio_do_cultivo):
        """Metodo construtor da classe
        """
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.inicio_do_cultivo = inicio_do_cultivo
    
    def json(self):
        """Transforma o objeto em um json

        Retorno:
            json: Objeto representado em json
        """
        return {
            'id': self.id,
            'nome': self.nome,
            'especie': self.especie,
            'localizacao': self.localizacao,
            'inicio_do_cultivo': str(self.inicio_do_cultivo)
        }
    
    def atualizar_planta(self, nome, especie, localizacao, inicio_do_cultivo):
        """Reconstroi o objeto com atributos atualizados
        """
        self.nome = nome
        self.especie = especie
        self.localizacao = localizacao
        self.inicio_do_cultivo = inicio_do_cultivo
    
    @classmethod
    def formatar_data(cls, dados):
        """Formata a data de entrada em inicio_do_cultivo para o metodo date da biblioteca datetime
        
        Argumentos:
            dados (dicionario): Dicionario com argumentos enviados pelo metodo POST e PATCH

        Retorno:
            dicionario: Dicionario com objeto 'date type' em inicio_do_cultivo
        """
        data = dados['inicio_do_cultivo'].split('-')
        data = list(map(int, data))
        dados['inicio_do_cultivo'] = date(data[0],data[1], data[2])
        return dados
    
    @classmethod
    def validar_argumentos(cls, dados):
        """Metodo de classe responsavel por validar se o argumento inicio_do_cultivo foi enviado

        Argumentos:
            dados (dicionario): argumentos enviados pelo metodo POST

        Retorno:
            booleano: Tipo de dado que pode ser True ou False
        """
        argumentos = dados.copy()
        if argumentos['inicio_do_cultivo']:
            return True
        return False
