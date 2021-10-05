from app import ma
from ..schemas import pergunta_schema
from ..models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario

    id_user = fields.Integer()
    id_sala = fields.Integer(default=None, allow_none=True, missing=None)

    perguntas = fields.List(
        fields.Nested(
            pergunta_schema.PerguntaSchema(exclude=['id_usuario'])
        )
    )
