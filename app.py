from flask import Flask
from config import Config
from models import db
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.turma_controller import TurmaController


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Cria Tabelas
with app.app_context():
    db.create_all()

# Rotas Alunos
app.add_url_rule("/alunos", view_func=AlunoController.listar_alunos, methods=["GET"])
app.add_url_rule("/alunos", view_func=AlunoController.criar_aluno, methods=["POST"])
app.add_url_rule("/alunos/atualizar/<int:aluno_id>", view_func=AlunoController.atualizar_aluno, methods=["PUT"])
app.add_url_rule("/alunos/deletar/<int:aluno_id>", view_func=AlunoController.deletar_aluno, methods=["DELETE"])

# Rotas Professores
app.add_url_rule("/professores", view_func=ProfessorController.listar_professores, methods=["GET"])
app.add_url_rule("/professores", view_func=ProfessorController.criar_professor, methods=["POST"])
app.add_url_rule("/professores/atualizar/<int:professor_id>", view_func=ProfessorController.atualizar_professor, methods=["PUT"])
app.add_url_rule("/professores/deletar/<int:professor_id>", view_func=ProfessorController.deletar_professor, methods=["DELETE"])

# Rotas Turmas
app.add_url_rule("/turmas", view_func=TurmaController.listar_turmas, methods=["GET"])
app.add_url_rule("/turmas", view_func=TurmaController.criar_turma, methods=["POST"])
app.add_url_rule("/turmas/atualizar/<int:turma_id>", view_func=TurmaController.atualizar_turma, methods=["PUT"])
app.add_url_rule("/turmas/deletar/<int:turma_id>", view_func=TurmaController.deletar_turma, methods=["DELETE"])


if __name__ == '__main__':
    app.run(debug=True, port=5000)