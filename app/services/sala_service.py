from .usuario_service import listar_usuario_id
from ..models import sala_model
from app import db

def cadastrar_sala(sala):
    sala_new = sala_model.Sala(
        id_moderador=sala['id_moderador'],
        nome_sala=sala['nome_sala'],
        descricao_sala=sala['descricao_sala'],
        tempo_mensagem=0,
        )

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
    
    if sala['nome_sala'] is not None:
        sala_bd.nome_sala = sala['nome_sala']
    if sala['descricao_sala'] is not None:
        sala_bd.descricao_sala = sala['descricao_sala']
    if sala['tempo_mensagem'] is not None:
        sala_bd.tempo_mensagem = sala['tempo_mensagem']

    db.session.commit()

def deletar_sala(sala):
    db.session.delete(sala)
    db.session.commit()

def banir_participante(id_sala, id_usuario):
    sala = listar_sala_id(id_sala)
    usuario = listar_usuario_id(id_usuario)

    if usuario in sala.banidos:
        sala.banidos.remove(usuario)
    else:
        sala.banidos.append(usuario)
        
    db.session.commit()
    return sala