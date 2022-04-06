from flask_restful import Resource, reqparse
from api.modelos.irrigador import ModeloIrrigador
from api.manipuladores.manipulador import Manipulador


manipulador = Manipulador()

class Irrigador(Resource):
    """Recurso Irrigador da api que herda de Resource da biblioteca flask_restful

    Argumento:
        Resource (class): Representação abstrata de um recurso RESTful
    """
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str, help="O campo 'nome' deve ser do tipo string.")
    args.add_argument('localizacao', type=str, help="O campo 'localizacao' deve ser do tipo string.")
    args.add_argument('temporizador', type=int, help="O campo 'especie' deve ser do tipo inteiro.")
    args.add_argument('duracao_da_irrigacao', type=int, help="O campo 'duracao_da_irrigacao' deve ser do tipo inteiro.")

    def get(self, id=None):
        """Metodo GET, busca objeto(s) no banco de dados e devolve-o(s) ao requisitante

        Argumento:
            id (None, Inteiro): id do objeto a ser buscado. Por padrão: None.

        Retornos:
            json: objeto buscado e o codigo 200
            tupla: contem um dicionario com uma mensagem de erro e o codigo 404
            tupla: contem um dicionario com uma lista com todos os objetos pedidos e o codigo 200
        """
        if id:
            irrigador = manipulador.localizar_objeto(ModeloIrrigador, id)
            if irrigador:
                simulacao = ModeloIrrigador.simular_irrigador()
                irrigador.irrigando, irrigador.voltagem = simulacao.values()
                return irrigador.json(), 200
            return {'mensagem': 'Irrigador não encontrado.'}, 404
        irrigadores = {
            'irrigadores': [irrigador.json() for irrigador in ModeloIrrigador.query.all()]
        }
        return irrigadores, 200
    
    def post(self):
        """Metodo POST, cria um objeto no banco de dados

        Retornos:
            tupla: dicionario com uma mensagem e o codigo 400
            tupla: dicionario com uma mensagem e o codigo 500
            tupla: dicionario com uma mensagem, o irrigador criado e o codigo 201
        """
        dados = Irrigador.args.parse_args()
        if not ModeloIrrigador.verificar_argumentos(dados):
            return {'mensagem': "Os argumentos 'nome', 'temporizador' e 'duracao_da_irrigacao' não podem ficar em branco."}, 400
        simulacao = ModeloIrrigador.simular_irrigador()
        irrigador = ModeloIrrigador(**dados, **simulacao)
        try:
            manipulador.salvar_objeto(irrigador)
        except:
            return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar salvar o irrigador.'}, 500
        return {'mensagem': 'O irrigador foi cadastrado com sucesso!', 'irrigador': irrigador.json()}, 201

    def patch(self, id):
        """Metodo PATCH, atualiza um objeto no banco de dados

        Retornos:
            tupla: dicionario com uma mensagem e o codigo 500
            tupla: dicionario com uma mensagem, o irrigador criado e o codigo 200
            tupla: dicionario com uma mensagem e o codigo 404
            tupla: dicionario com uma mensagem e o codigo 400
        """
        if id:
            irrigador = manipulador.localizar_objeto(ModeloIrrigador, id)
            if irrigador:
                dados = Irrigador.args.parse_args()
                dados = manipulador.verificar_dados_vazios(irrigador, dados)
                simulacao = ModeloIrrigador.simular_irrigador()
                irrigador.atualizar_irrigador(**dados, **simulacao)
                try:
                    manipulador.salvar_objeto(irrigador)
                except:
                    return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar atualizar o irrigador.'}, 500
                return {'mensagem': 'As confogurações do irrigador foram atualizadas.', 'irrigador': irrigador.json()}, 200
            return {'mensagem': 'Irrigador não encontrado.'}, 404
        return {'mensagem': "Requisição mal feito, o atributo 'id' é obrigatório."}, 400 

    def delete(self, id):
        """Metodo DELETE, deleta um objeto no banco de dados

        Retornos:
            tupla: dicionario com uma mensagem e o codigo 500
            tupla: dicionario com uma mensagem e o codigo 200
            tupla: dicionario com uma mensagem e o codigo 404
            tupla: dicionario com uma mensagem e o codigo 400
        """
        if id:
            irrigador = manipulador.localizar_objeto(ModeloIrrigador, id)
            if irrigador:
                try:
                    manipulador.deletar_objeto(irrigador)
                except:
                    return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar deletar o irrigador.'}, 500
                return {'mensagem': 'Irrigador Deletado.'}, 200
            return {'mensagem': 'Irrigador não encontrado.'}, 404
        return {'mensagem': "Requisição mal feito, o atributo 'id' é obrigatório."}, 400 