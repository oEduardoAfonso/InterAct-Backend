from .usuario_service import listar_usuario_id
from ..models import pergunta_model
from app import db

def cadastrar_pergunta(pergunta):
    pergunta_new = pergunta_model.Pergunta(
        conteudo=pergunta['conteudo'],
        is_respondida=pergunta['is_respondida'],
        id_usuario=pergunta['id_usuario'],
        id_sala=pergunta['id_sala']
    )

    db.session.add(pergunta_new)
    db.session.commit()
    return pergunta_new

def listar_perguntas():
    perguntas = pergunta_model.Pergunta.query.all()
    return perguntas

def listar_pergunta_id(id):
    pergunta = pergunta_model.Pergunta.query.filter_by(id_pergunta=id).first()
    return pergunta

def editar_pergunta(pergunta_bd, pergunta):
    pergunta_new = pergunta_model.Pergunta(
        is_respondida=pergunta['is_respondida'],
    )

    pergunta_bd.is_respondida = pergunta_new.is_respondida

    db.session.commit()

def deletar_pergunta(pergunta):
    db.session.delete(pergunta)
    db.session.commit()

def concordar_pergunta(id_pergunta, id_usuario):
    usuario = listar_usuario_id(id_usuario)
    pergunta = listar_pergunta_id(id_pergunta)

    if usuario in pergunta.concordaram:
        pergunta.concordaram.remove(usuario)
    else:
        pergunta.concordaram.append(usuario)
        
    db.session.commit()
    return pergunta