from flask_restful import Resource, reqparse
from api.models.regador import RegadorModel


class Regador(Resource):
    args = reqparse.RequestParser()
    args.add_argument('nome', type=str)
    args.add_argument('localizacao', type=str)
    args.add_argument('temporizador', type=int)

    def get(self, id=None):
        if id:
            regador = RegadorModel.find_regador(id)
            if regador:
                return regador.json()
            return {'message': 'Regador not found.'}, 404
        regadores = {
            'regadores': [regador.json() for regador in RegadorModel.query.all()]
        }
        return regadores
    
    def post(self):
        dados = Regador.args.parse_args()
        simulacao = RegadorModel.simula_funcionamento()
        regador = RegadorModel(**dados, **simulacao)
        try:
            regador.save_regador()
        except:
            return {'message': 'An internal error ocurred trying to save regador.'}, 500
        return regador.json()

    def patch(self, id):
        regador = RegadorModel.find_regador(id)
        if regador:
            dados = Regador.args.parse_args()
            dados_formatados = regador.format_data(dados)
            simulacao = RegadorModel.simula_funcionamento()
            regador.update_regador(**dados_formatados, **simulacao)
            try:
                regador.save_regador()
            except:
                return {'message': 'An internal error ocurred trying to update regador.'}, 500
            return regador.json(), 200
        return {'message': 'Planta not found.'}, 404
            
    def delete(self, id):
        regador = RegadorModel.find_regador(id)
        if regador:
            try:
                regador.delete_regador()
            except:
                return {'message': 'An internal error ocurred trying to delete regador.'}, 500
            return {'message': 'Regador deleted.'}, 200
        return {'message': 'Regador not found.'}, 404