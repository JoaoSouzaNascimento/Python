from flask import Flask, render_template
from flask_migrate import Migrate

from database import db
from usuarios import bp_usuarios

app = Flask(__name__)

conexao = 'sqlite:///meubanco.sqlite'

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.sqlite' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def index():
  return render_template('usuarios_menu.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)