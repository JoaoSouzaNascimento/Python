from flask import Blueprint, render_template, request, redirect
from models import Usuario
from database import db

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates")

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('usuarios_create.html')

  if request.method=='POST':
    name = request.form.get('name')
    cpf = request.form.get('cpf')
    sex = request.form.get('sex')
    birth = request.form.get('birth')

    user = Usuario(name, cpf, sex, birth)
    db.session.add(user)
    db.session.commit()
    return 'Dados Cadastrados com sucesso'

@bp_usuarios.route('/recovery')
def recovery():
  usuarios = Usuario.query.all()
  return render_template('usuarios_recovery.html',usuarios = usuarios)

@bp_usuarios.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
  u = Usuario.query.get(id)
  
  if request.method=='GET':
    return render_template('usuarios_update.html', u = u)

  if request.method=='POST':
    name = request.form.get('name')
    cpf = request.form.get('cpf')
    sex = request.form.get('sex')
    birth = request.form.get('birth')

    u.name = name
    u.cpf = cpf
    u.sex = sex
    u.birth = birth

    db.session.add(u)
    db.session.commit()
    return redirect('/usuarios/recovery')

@bp_usuarios.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
  u = Usuario.query.get(id)

  if request.method=='GET':
    return render_template('usuarios_delete.html', u = u)

  if request.method=='POST':
    db.session.delete(u)
    db.session.commit()
    return redirect('/usuarios/recovery')