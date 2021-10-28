from app import ma
from . import usuario_schema, pergunta_schema
from ..models import sala_model
from marshmallow import fields, validate

class SalaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = sala_model.Sala

    id_sala = fields.Integer()
    id_moderador = fields.Integer()
    nome_sala = fields.String(allow_none=True, missing=None, validate=validate.Length(min=1, max=30))
    descricao_sala = fields.String(allow_none=True, missing=None, validate=validate.Length(max=30))
    tempo_mensagem = fields.Integer(allow_none=True, missing=None)

    participantes = fields.List(
        fields.Nested(
            usuario_schema.UsuarioSchema(exclude=['id_sala'])
        )
    )

    banidos = fields.List(
        fields.Nested(
            usuario_schema.UsuarioSchema(only=['id_usuario'])
        )
    )

    perguntas = fields.List(
        fields.Nested(
            pergunta_schema.PerguntaSchema(exclude=['id_sala'])
        )
    )