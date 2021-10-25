from flask_restful import Resource
from flask.helpers import make_response
from app import api, io
from flask_socketio import emit
from ..schemas import pergunta_schema, sala_schema
from ..services import pergunta_service, sala_service
from flask import request, jsonify

class PerguntaList(Resource):
    def get(self):
        ps = pergunta_schema.PerguntaSchema(many=True)
        perguntas = pergunta_service.listar_perguntas()

        return make_response(ps.jsonify(perguntas), 200)

    def post(self):
        ps = pergunta_schema.PerguntaSchema()
        pergunta = ps.load(request.json)
        resultado = pergunta_service.cadastrar_pergunta(pergunta)
        
        return make_response(ps.jsonify(resultado), 201)

class PerguntaDetail(Resource):
    def get(self, id):
        ps = pergunta_schema.PerguntaSchema()
        pergunta = pergunta_service.listar_pergunta_id(id)

        if pergunta is None:
            return make_response(jsonify('Pergunta nao encontrada'), 404)
        return make_response(ps.jsonify(pergunta), 200)

    def put(self, id):
        pergunta_bd = pergunta_service.listar_pergunta_id(id)
        if pergunta_bd is None:
            return make_response(jsonify('Pergunta nao encontrada'), 404)

        ps = pergunta_schema.PerguntaSchema()
        pergunta = ps.load(request.json)
        pergunta_service.editar_pergunta(pergunta_bd, pergunta)

        pergunta_editada = pergunta_service.listar_pergunta_id(id)

        return make_response(ps.jsonify(pergunta_editada), 200)

    def delete(self, id):
        pergunta = pergunta_service.listar_pergunta_id(id)
        if pergunta is None:
            return make_response(jsonify('Pergunta nao encontrada'), 404)

        pergunta_service.deletar_pergunta(pergunta)
        return make_response('', 204)

class ConcordarPergunta(Resource):
    def post(self, id):
        ps_id = pergunta_schema.PerguntaSchema(only=['id_usuario'])
        id_usuario = ps_id.load(request.json).get('id_usuario')

        pergunta = pergunta_service.concordar_pergunta(id, id_usuario)
        ps = pergunta_schema.PerguntaSchema()
        return make_response(ps.jsonify(pergunta), 200)

@io.on('envia.pergunta')
def envia_pergunta_handler(pergunta):
    pergunta_service.cadastrar_pergunta(pergunta)
    sala = sala_service.listar_sala_id(pergunta['id_sala'])
    ss = sala_schema.SalaSchema()
    perguntas = ss.jsonify(sala).json['perguntas']
    emit('recebe.perguntas', perguntas, json=True , broadcast=True)

@io.on('concorda.pergunta')
def concordar_pergunta_handler(concordar):
    pergunta_service.concordar_pergunta(concordar['id_pergunta'], concordar['id_usuario'])
    sala = sala_service.listar_sala_id(concordar['id_sala'])
    ss = sala_schema.SalaSchema()
    perguntas = ss.jsonify(sala).json['perguntas']
    emit('recebe.perguntas', perguntas, json=True , broadcast=True)

@io.on('ler.pergunta')
def ler_pergunta_handler(pergunta):
    pergunta_bd = pergunta_service.listar_pergunta_id(pergunta['id_pergunta'])
    respondida = {"is_respondida": True}
    pergunta_service.editar_pergunta(pergunta_bd, respondida)

    sala = sala_service.listar_sala_id(pergunta['id_sala'])
    ss = sala_schema.SalaSchema()
    perguntas = ss.jsonify(sala).json['perguntas']
    emit('recebe.perguntas', perguntas, json=True , broadcast=True)

api.add_resource(PerguntaList, '/perguntas')
api.add_resource(PerguntaDetail, '/perguntas/<int:id>')
api.add_resource(ConcordarPergunta, '/perguntas/concordar/<int:id>')