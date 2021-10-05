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
        nullable=False,
    )

    is_respondida = db.Column(
        'is_respondida',
        db.Boolean,
        nullable=False,
    )

    likes = db.Column(
        'likes',
        db.Integer,
        nullable=False,
        default=0,
    )

    id_usuario = db.Column(
        'id_usuario',
        db.Integer,
        db.ForeignKey('usuario.id_user'),
        nullable=False,
    )

    autor = db.relationship('Usuario', foreign_keys=[id_usuario], backref='perguntas')

    id_sala = db.Column(
        'id_sala',
        db.Integer,
        db.ForeignKey('sala.id_sala'),
        nullable=False,
    )

    sala = db.relationship('Sala', foreign_keys=[id_sala], backref='perguntas')