from app import ma
from ..models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.Usuario

    id_user = fields.Integer()
    id_sala = fields.Integer()
