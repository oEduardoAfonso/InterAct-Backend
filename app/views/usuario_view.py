from flask_restful import Resource
from app import api

class UsuarioList(Resource):
    def get(self):
        return 'Ola mundo, usuarios'

api.add_resource(UsuarioList, '/usuarios')
