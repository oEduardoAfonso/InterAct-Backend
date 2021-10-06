from app import ma
from ..schemas import usuario_schema
from ..models import pergunta_model
from marshmallow import fields, validate

class PerguntaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = pergunta_model.Pergunta

    id_pergunta = fields.Integer()
    conteudo = fields.String(required=True, validate=validate.Length(min=1, max=200))
    data_hora = fields.DateTime()
    is_respondida = fields.Boolean(allow_none=True, missing=None)
    id_usuario = fields.Integer(required=True)
    id_sala = fields.Integer(required=True)

    concordaram = fields.List(
        fields.Nested(
            usuario_schema.UsuarioSchema(only=['id_usuario'])
        )
    )