from flask_restful import Resource
from flask.helpers import make_response
from app import api
from ..schemas import pergunta_schema
from ..services import pergunta_service
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


api.add_resource(PerguntaList, '/perguntas')
api.add_resource(PerguntaDetail, '/perguntas/<int:id>')