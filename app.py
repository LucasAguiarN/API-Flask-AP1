import os
from flask import Flask
from config import Config
from models import db
#from controllers.aluno import Aluno
#from controllers.professor import Professor
#from controllers.turma import Turma
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

db.init_app(app)

# Cria Tabelas
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=5000)