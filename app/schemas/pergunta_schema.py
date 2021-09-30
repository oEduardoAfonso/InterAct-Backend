from app import ma
from models import pergunta_model
from marshmallow import fields

class PerguntaSchema(ma.ModelSchema):
    class Meta:
        model = pergunta_model.Pergunta
        fields = (
            'id_pergunta',
            'data_hora',
            'is_respondida',
            'likes',
            'id_usuario',
            'id_sala'
        )

    data_hora = fields.DateTime(auto_now_add=True, required=True)
    is_respondida = fields.Boolean(required=True)
    likes = fields.Integer(required=True)
    id_usuario = fields.Integer(required=True)
    id_sala = fields.Integer(required=True)