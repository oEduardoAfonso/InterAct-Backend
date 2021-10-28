from flask_restful import Resource
from flask.helpers import make_response
from app import api, io
from flask_socketio import emit
from ..schemas import mensagem_schema, sala_schema
from ..services import mensagem_service, sala_service
from flask import request, jsonify

class MensagemList(Resource):
    def get(self):
        ms = mensagem_schema.MensagemSchema(many=True)
        mensagens = mensagem_service.listar_mensagens()

        return make_response(ms.jsonify(mensagens), 200)

    def post(self):
        ms = mensagem_schema.MensagemSchema()
        mensagem = ms.load(request.json)
        resultado = mensagem_service.cadastrar_mensagem(mensagem)
        
        return make_response(ms.jsonify(resultado), 201)

class MensagemDetail(Resource):
    def get(self, id):
        ms = mensagem_schema.MensagemSchema()
        mensagem = mensagem_service.listar_mensagem_id(id)

        if mensagem is None:
            return make_response(jsonify('mensagem nao encontrada'), 404)
        return make_response(ms.jsonify(mensagem), 200)

    def put(self, id):
        mensagem_bd = mensagem_service.listar_mensagem_id(id)
        if mensagem_bd is None:
            return make_response(jsonify('mensagem nao encontrada'), 404)

        ms = mensagem_schema.MensagemSchema()
        mensagem = ms.load(request.json)
        mensagem_service.editar_mensagem(mensagem_bd, mensagem)

        mensagem_editada = mensagem_service.listar_mensagem_id(id)

        return make_response(ms.jsonify(mensagem_editada), 200)

    def delete(self, id):
        mensagem = mensagem_service.listar_mensagem_id(id)
        if mensagem is None:
            return make_response(jsonify('mensagem nao encontrada'), 404)

        mensagem_service.deletar_mensagem(mensagem)
        return make_response('', 204)

@io.on('envia.mensagem')
def envia_mensagem_handler(mensagem):
    mensagem_service.cadastrar_mensagem(mensagem)
    sala = sala_service.listar_sala_id(mensagem['id_sala'])
    ss = sala_schema.SalaSchema()
    mensagens = ss.jsonify(sala).json['mensagens']
    emit('recebe.mensagens', mensagens, json=True , broadcast=True)

api.add_resource(MensagemList, '/mensagens')
api.add_resource(MensagemDetail, '/mensagens/<int:id>')