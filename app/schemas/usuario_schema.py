from app import ma
from ..models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario

    id_usuario = fields.Integer()
    nome_usuario = fields.String()
    id_sala = fields.Integer(default=None, allow_none=True, missing=None)

class UsuariosConcordam(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.UsuariosConcordam

    id_pergunta = fields.Integer()
    id_usuario = fields.Integer()