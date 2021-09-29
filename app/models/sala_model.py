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
    )