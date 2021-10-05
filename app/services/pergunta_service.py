from ..models import pergunta_model
from app import db

def cadastrar_pergunta(pergunta):
    pergunta_new = pergunta_model.Pergunta(
        conteudo=pergunta['conteudo'],
        data_hora=pergunta['data_hora'],
        is_respondida=pergunta['is_respondida'],
        likes=pergunta['likes'],
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
        conteudo=pergunta['conteudo'],
        data_hora=pergunta['data_hora'],
        is_respondida=pergunta['is_respondida'],
        likes=pergunta['likes'],
        id_usuario=pergunta['id_usuario'],
        id_sala=pergunta['id_sala']
    )

    pergunta_bd.conteudo = pergunta_new.conteudo
    pergunta_bd.data_hora = pergunta_new.data_hora
    pergunta_bd.is_respondida = pergunta_new.is_respondida
    pergunta_bd.likes = pergunta_new.likes
    pergunta_bd.id_usuario = pergunta_new.id_usuario
    pergunta_bd.id_sala = pergunta_new.id_sala

    db.session.commit()

def deletar_pergunta(pergunta):
    db.session.delete(pergunta)
    db.session.commit()