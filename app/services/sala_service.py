from ..models import sala_model
from app import db

def cadastrar_sala(sala):
    sala_new = sala_model.Sala(id_moderador=sala['id_moderador'])

    db.session.add(sala_new)
    db.session.commit()
    return sala_new

def listar_salas():
    salas = sala_model.Sala.query.all()
    return salas

def listar_sala_id(id):
    sala = sala_model.Sala.query.filter_by(id_sala=id).first()
    return sala

def editar_sala(sala_bd, sala):
    sala_new = sala_model.Sala(id_moderador=sala['id_moderador'])

    sala_bd.id_moderador = sala_new.id_moderador
    db.session.commit()

def deletar_sala(sala):
    db.session.delete(sala)
    db.session.commit()