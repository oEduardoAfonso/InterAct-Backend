from ..models import mensagem_model
from app import db

def cadastrar_mensagem(mensagem):
    mensagem_new = mensagem_model.Mensagem(
        conteudo=mensagem['conteudo'],
        id_usuario=mensagem['id_usuario'],
        id_sala=mensagem['id_sala']
    )

    db.session.add(mensagem_new)
    db.session.commit()
    return mensagem_new

def listar_mensagens():
    mensagens = mensagem_model.Mensagem.query.all()
    return mensagens

def listar_mensagem_id(id):
    mensagem = mensagem_model.Mensagem.query.filter_by(id_mensagem=id).first()
    return mensagem

def editar_mensagem(mensagem_bd, mensagem):
    mensagem_new = mensagem_model.Mensagem(
        conteudo=mensagem['conteudo'],
    )

    mensagem_bd.conteudo = mensagem_new.conteudo

    db.session.commit()

def deletar_mensagem(mensagem):
    db.session.delete(mensagem)
    db.session.commit()
