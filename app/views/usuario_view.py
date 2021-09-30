from flask.helpers import make_response
from flask_restful import Resource
from app import api
from ..schemas import usuario_schema
from ..entitys import usuario
from ..services import usuario_service
from flask import json, request, make_response, jsonify

class UsuarioList(Resource):
    def get(self):
        us = usuario_schema.UsuarioSchema(many=True)
        usuarios = usuario_service.listar_usuarios()

        return make_response(us.jsonify(usuarios), 200)

    def post(self):
        us = usuario_schema.UsuarioSchema()
        usuario = us.load(request.json)

        result = usuario_service.cadastrar_usuario(usuario)
        return make_response(us.jsonify(result), 201)

class UsuarioDetail(Resource):
    def get(self, id):
        usuario = usuario_service.listar_usuario_id(id)
        if usuario is None:
            return make_response(jsonify('Usuário não encontrado'), 404)
        
        us = usuario_schema.UsuarioSchema()
        return make_response(us.jsonify(usuario), 200)

    def put(self, id):
        usuario_bd = usuario_service.listar_usuario_id(id)
        if usuario_bd is None:
            return make_response(jsonify('Usuário não encontrado'), 404)

        us = usuario_schema.UsuarioSchema()
        usuario = us.load(request.json)
        usuario_service.editar_usuario(usuario_bd, usuario)

        usuario_editado = usuario_service.listar_usuario_id(id)
        return make_response(us.jsonify(usuario_editado), 200)

    def delete(self, id):
        usuario = usuario_service.listar_usuario_id(id)
        if usuario is None:
            return make_response(jsonify('Usuário não encontrado'), 404)

        usuario_service.deletar_usuario(usuario)
        return make_response('', 204)



api.add_resource(UsuarioList, '/usuarios')
api.add_resource(UsuarioDetail, '/usuarios/<int:id>')