from sqlalchemy.orm import backref
from app import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    id_usuario = db.Column(
        'id_usuario',
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    nome_usuario = db.Column(
        'nome_usuario',
        db.String(100),
        nullable=False,
    )

    id_sala = db.Column(
        'id_sala',
        db.Integer,
        db.ForeignKey('sala.id_sala'),
        nullable=True,
    )

    sala_participa = db.relationship('Sala', foreign_keys=[id_sala], backref=backref('participantes'))
    concordou = db.relationship('Pergunta', secondary='usuarios_concordam', backref='concordaram')

class UsuariosConcordam(db.Model):
    __tablename__ = "usuarios_concordam"

    id_pergunta = db.Column(
        'id_pergunta',
        db.Integer,
        db.ForeignKey('pergunta.id_pergunta'),
        nullable=False,
        primary_key=True,
    )

    id_usuario = db.Column(
        'id_usuario',
        db.Integer,
        db.ForeignKey('usuario.id_usuario'),
        nullable=False,
        primary_key=True,
    )