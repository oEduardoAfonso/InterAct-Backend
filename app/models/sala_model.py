from sqlalchemy.orm import backref
from app import db

class Sala(db.Model):
    __tablename__ = "sala"

    id_sala = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    id_moderador = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id_user'),
        nullable=False,
        unique=True,
    )

    moderador = db.relationship('Usuario', foreign_keys=[id_moderador], cascade='all, delete')
    # usuarios = db.relationship('Usuario', foreign_keys=['usuario.id_sala'],  backref='id_sala')