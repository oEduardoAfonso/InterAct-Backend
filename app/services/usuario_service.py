from ..models import usuario_model
from app import db

def cadastrar_usuario(usuario):
    usuario_new = usuario_model.Usuario(id_sala=usuario['id_sala'])

    db.session.add(usuario_new)
    db.session.commit()
    return usuario_new

def listar_usuarios():
    usuarios = usuario_model.Usuario.query.all()
    return usuarios

def listar_usuario_id(id):
    usuario = usuario_model.Usuario.query.filter_by(id_usuario=id).first()
    return usuario

def editar_usuario(usuario_bd, usuario):
    usuario_new = usuario_model.Usuario(id_sala=usuario['id_sala'])

    usuario_bd.id_sala = usuario_new.id_sala
    db.session.commit()

def deletar_usuario(usuario):
    if(usuario.id_usuario == usuario.sala_participa.id_moderador):
        db.session.delete(usuario.sala_participa)
    db.session.delete(usuario)
    db.session.commit()