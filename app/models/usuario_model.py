from app import db
from . import sala_model

class Usuario(db.Model):
    __tablename__ = "usuario"

    id_user = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    id_sala = db.Column(
        db.Integer,
        db.ForeignKey('sala.id_sala'),
        nullable=True,
    )