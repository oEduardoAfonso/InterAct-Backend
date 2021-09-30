from app import ma
from models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.ModelSchema):
    class Meta:
        model = usuario_model.Usuario
        field = (
            'id_user',
            'id_sala'
        )
    
    id_sala = fields.Integer(required=False)
