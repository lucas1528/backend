from flask_restful import Resource
from flask import redirect


class Documentacao(Resource):
    def get(self):
        documentacao = 'https://documenter.getpostman.com/view/20248101/UVyuTayN'
        return redirect(documentacao)