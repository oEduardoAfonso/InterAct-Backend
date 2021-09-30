from app import ma
from models import sala_model
from marshmallow import fields

class SalaSchema(ma.ModelSchema):
    class Meta:
        model = sala_model.Sala
        fields = (
            'id_sala',
            'id_moderador'
        )

    id_moderador = fields.Integer(required=True)