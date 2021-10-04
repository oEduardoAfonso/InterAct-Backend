from sqlalchemy.orm import backref
from app import db

class Pergunta(db.Model):
    __tablename__ = "pergunta"

    id_pergunta = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    data_hora = db.Column(
        db.DateTime,
        nullable=False,
    )

    is_respondida = db.Column(
        db.Boolean,
        nullable=False,
    )

    likes = db.Column(
        db.Integer,
        nullable=False,
        default=0,
    )

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id_user'),
        nullable=False,
    )

    autor = db.relationship('Usuario', foreign_keys=['id_usuario'], backref='perguntas')

    id_sala = db.Column(
        db.Integer,
        db.ForeignKey('sala.id_sala'),
        nullable=False,
    )

    autor = db.relationship('Sala', foreign_keys=['id_sala'], backref='perguntas')