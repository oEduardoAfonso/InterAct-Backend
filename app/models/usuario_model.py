from sqlalchemy.orm import backref
from app import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    id_user = db.Column(
        'id_user',
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    id_sala = db.Column(
        'id_sala',
        db.Integer,
        db.ForeignKey('sala.id_sala'),
        nullable=True,
    )

    sala_participa = db.relationship('Sala', foreign_keys=[id_sala], backref=backref('participantes'))