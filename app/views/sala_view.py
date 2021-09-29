from flask_restful import Resource
from app import api

class SalaList(Resource):
    def get(self):
        return 'Ola mundo, sala'

api.add_resource(SalaList, '/salas')
