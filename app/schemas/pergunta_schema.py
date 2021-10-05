from app import ma
from ..models import pergunta_model
from marshmallow import fields, validate

class PerguntaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = pergunta_model.Pergunta

    id_pergunta = fields.Integer()
    conteudo = fields.String(required=True, validate=validate.Length(min=1, max=200))
    data_hora = fields.DateTime(auto_now_add=True, required=True)
    is_respondida = fields.Boolean(required=True)
    likes = fields.Integer(default=0, allow_none=True, missing=0)
    id_usuario = fields.Integer(required=True)
    id_sala = fields.Integer(required=True)