from datetime import datetime

from sqlalchemy.orm import backref
from app import db

class Pergunta(db.Model):
    __tablename__ = "pergunta"

    id_pergunta = db.Column(
        'id_pergunta',
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    conteudo = db.Column(
        'conteudo',
        db.String(200),
        nullable=False,
    )

    data_hora = db.Column(
        'data_hora',
        db.DateTime,
        default=datetime.now(),
        nullable=False,
    )

    is_respondida = db.Column(
        'is_respondida',
        db.Boolean,
        default=False,
        nullable=False,
    )

    id_usuario = db.Column(
        'id_usuario',
        db.Integer,
        db.ForeignKey('usuario.id_usuario'),
        nullable=False,
    )

    autor = db.relationship('Usuario', foreign_keys=[id_usuario], backref=backref('perguntas', cascade='all,delete'))

    id_sala = db.Column(
        'id_sala',
        db.Integer,
        db.ForeignKey('sala.id_sala'),
        nullable=False,
    )

    sala = db.relationship('Sala', foreign_keys=[id_sala], backref=backref('perguntas', cascade='all,delete'))