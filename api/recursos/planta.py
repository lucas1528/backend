from flask_restful import Resource, reqparse
from api.modelos.planta import ModeloPlanta
from api.manipuladores.manipulador import Manipulador


manipulador = Manipulador()

class Planta(Resource):
    """Recurso Planta da api que herda de Resource da biblioteca flask_restful

    Argumento:
        Resource (class): Representação abstrata de um recurso RESTful
    """
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ficar em branco.")
    args.add_argument('especie', type=str, help="O campo 'especie' deve ser do tipo string.")
    args.add_argument('localizacao', type=str, help="O campo 'localizacao' deve ser do tipo string.")
    args.add_argument('inicio_do_cultivo', type=str, help="O campo 'inicio_do_cultivo' deve ser do tipo string no seguinte formato -> YYYY-mm-dd")

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
            planta = manipulador.localizar_objeto(ModeloPlanta, id)
            if planta:
                return planta.json(), 200
            return {'mensagem': 'Planta não encontrada.'}, 404
        plantas = {
            'plantas': [planta.json() for planta in ModeloPlanta.query.all()]
        }
        return plantas, 200
    
    def post(self):
        """Metodo POST, cria um objeto no banco de dados

        Retornos:
            tupla: dicionario com uma mensagem e o codigo 500
            tupla: dicionario com uma mensagem, a planta criada e o codigo 201
        """
        dados = Planta.args.parse_args()
        if ModeloPlanta.validar_argumentos(dados):
            dados = ModeloPlanta.formatar_data(dados)
        planta = ModeloPlanta(**dados)
        try:
            manipulador.salvar_objeto(planta)
        except:
            return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar salvar a planta.'}, 500
        return {'mensagem': 'A planta foi cadastrada com sucesso!', 'planta': planta.json()}, 201
        
    def patch(self, id):
        """Metodo PATCH, atualiza um objeto no banco de dados

        Retornos:
            tupla: dicionario com uma mensagem e o codigo 500
            tupla: dicionario com uma mensagem, o irrigador criado e o codigo 200
            tupla: dicionario com uma mensagem e o codigo 404
            tupla: dicionario com uma mensagem e o codigo 400
        """
        if id:
            planta = manipulador.localizar_objeto(ModeloPlanta, id)
            if planta:
                dados = Planta.args.parse_args()
                dados = manipulador.verificar_dados_vazios(planta, dados)
                dados = ModeloPlanta.formatar_data(dados)
                planta.atualizar_planta(**dados)
                try:
                    manipulador.salvar_objeto(planta)
                except:
                    return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar atualizar a planta.'}, 500
                return {'mensagem': 'As informações da planta foram atualizados.', 'planta': planta.json()}, 200
            return {'mensagem': 'Planta não encontrada.'}, 404
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
            planta = manipulador.localizar_objeto(ModeloPlanta, id)
            if planta:
                try:
                    manipulador.deletar_objeto(planta)
                except:
                    return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar deletar a planta.'}, 500
                return {'mensagem': 'Planta deletada.'}, 200
            return {'mensagem': 'Planta não encontrada.'}, 404
        return {'mensagem': "Requisição mal feito, o atributo 'id' é obrigatório."}, 400  