from flask.helpers import make_response
from flask_restful import Resource
from app import api
from ..schemas import sala_schema, usuario_schema
from ..services import sala_service, usuario_service
from flask import request, jsonify

class SalaList(Resource):
    def get(self):
        ss = sala_schema.SalaSchema(many=True)
        salas = sala_service.listar_salas()

        return make_response(ss.jsonify(salas), 200)

    def post(self):
        ss = sala_schema.SalaSchema()
        sala = ss.load(request.json)

        resultado = sala_service.cadastrar_sala(sala)

        moderador = usuario_service.listar_usuario_id(sala['id_moderador'])   
        moderador_new  = {'id_sala': resultado.id_sala}
        usuario_service.editar_usuario(moderador, moderador_new)

        return make_response(ss.jsonify(resultado), 201)

class SalaDetail(Resource):
    def get(self, id):
        sala = sala_service.listar_sala_id(id)

        if sala is None:
            return make_response(jsonify('Sala nao encontrada'), 404)

        ss = sala_schema.SalaSchema()
        return make_response(ss.jsonify(sala), 200)

    def put(self, id):
        sala_bd = sala_service.listar_sala_id(id)
        if sala_bd is None:
            return make_response(jsonify('Sala nao encontrada'), 404)

        ss = sala_schema.SalaSchema()
        sala = ss.load(request.json)
        sala_service.editar_sala(sala_bd, sala)

        sala_editada = sala_service.listar_sala_id(id)
        return make_response(ss.jsonify(sala_editada), 200)

    def delete(self, id):
        sala = sala_service.listar_sala_id(id)
        if sala is None:
            return make_response(jsonify('Sala nao encontrada'), 404)

        sala_service.deletar_sala(sala)
        return make_response('', 204)

class BanirParticipante(Resource):
    def post(self, id):
        us_id = usuario_schema.UsuarioSchema(only=['id_usuario'])
        id_usuario = us_id.load(request.json).get('id_usuario')

        sala = sala_service.banir_participante(id, id_usuario)
        ss = sala_schema.SalaSchema()
        return make_response(ss.jsonify(sala), 200)

api.add_resource(SalaList, '/salas')
api.add_resource(SalaDetail, '/salas/<int:id>')
api.add_resource(BanirParticipante, '/salas/banir/<int:id>')
