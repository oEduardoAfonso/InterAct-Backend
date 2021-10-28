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

    nome_sala = db.Column(
        'nome_sala',
        db.String(30),
        nullable=False,
    )

    descricao_sala = db.Column(
        'descricao_sala',
        db.String(150),
    )

    tempo_mensagem = db.Column(
        'tempo_mensagem',
        db.Integer,
        nullable=False,
    )

    moderador = db.relationship('Usuario', foreign_keys=[id_moderador], backref=backref('sala_modera', cascade='all,delete'))

class Participantes_Banidos(db.Model):
    __tablename__ = "participantes_banidos"

    id_sala = db.Column(
        'id_sala',
        db.Integer,
        db.ForeignKey('sala.id_sala'),
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