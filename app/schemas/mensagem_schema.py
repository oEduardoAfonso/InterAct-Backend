from app import ma
from ..models import mensagem_model
from marshmallow import fields, validate

class MensagemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = mensagem_model.Mensagem

    id_mensagem = fields.Integer()
    conteudo = fields.String(required=True, validate=validate.Length(min=1, max=200))
    data_hora = fields.DateTime()
    id_usuario = fields.Integer(required=True)
    id_sala = fields.Integer(required=True)
