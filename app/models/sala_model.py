from sqlalchemy.orm import backref
from app import db

class Sala(db.Model):
    __tablename__ = "sala"

    id_sala = db.Column(
        'id_sala',
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    id_moderador = db.Column(
        'id_moderador',
        db.Integer,
        db.ForeignKey('usuario.id_usuario'),
        nullable=False,
        unique=True,
    )

    moderador = db.relationship('Usuario', foreign_keys=[id_moderador], backref=backref('sala_modera', cascade='all,delete'))