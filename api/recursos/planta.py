from flask_restful import Resource, reqparse
from api.modelos.planta import ModeloPlanta
from api.manipuladores.manipulador import Manipulador


manipulador = Manipulador()

class Planta(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ficar em branco.")
    args.add_argument('especie', type=str, help="O campo 'especie' deve ser do tipo string.")
    args.add_argument('localizacao', type=str, help="O campo 'localizacao' deve ser do tipo string.")
    args.add_argument('inicio_do_cultivo', type=str, help="O campo 'inicio_do_cultivo' deve ser do tipo string no seguinte formato -> YYYY-mm-dd")

    def get(self, id=None):
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
        dados = Planta.args.parse_args()
        dados = ModeloPlanta.formatar_dada(dados)
        planta = ModeloPlanta(**dados)
        try:
            manipulador.salvar_objeto(planta)
        except:
            return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar salvar a planta.'}, 500
        return {'mensagem': 'A planta foi cadastrada com sucesso!', 'planta': planta.json()}, 201

    def patch(self, id):
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
            
    def delete(self, id):
        planta = manipulador.localizar_objeto(ModeloPlanta, id)
        if planta:
            try:
                manipulador.deletar_objeto(planta)
            except:
                return {'mensagem': 'Ocorreu um erro interno no servidor ao tentar deletar a planta.'}, 500
            return {'mensagem': 'Planta deletada.'}, 200
        return {'mensagem': 'Planta não encontrada.'}, 404