from app import db

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

    sala = db.relationship('Sala', foreign_keys=[id_sala], post_update=True)