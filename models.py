from database import db

class Usuario(db.Model):
  __tablename__="usuario"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  cpf = db.Column(db.String(100))
  sex = db.Column(db.String(100))
  birth = db.Column(db.String(100))

  def __init__(self,name,cpf,sex,birth):
    self.name = name
    self.cpf = cpf
    self.sex = sex
    self.birth = birth

  def __repr__(self):
    return "Usuario: {}".format(self.name)