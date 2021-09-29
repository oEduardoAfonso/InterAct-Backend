from flask_restful import Resource
from app import api

class PerguntaList(Resource):
    def get(self):
        return 'Ola mundo, perguntas'

api.add_resource(PerguntaList, '/perguntas')