from app import ma
from . import usuario_schema
from ..models import sala_model
from marshmallow import fields

class SalaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = sala_model.Sala

    id_sala = fields.Integer()
    id_moderador = fields.Integer(required=True)
    participantes = fields.List(
        fields.Nested(
            usuario_schema.UsuarioSchema(exclude=['id_sala'])
        )
    )