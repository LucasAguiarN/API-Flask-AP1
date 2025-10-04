from flask import Flask
from flasgger import Swagger
from config import Config
from models import db
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.turma_controller import TurmaController


app = Flask(__name__)
app.config.from_object(Config)
swagger = Swagger(app, template_file='swagger.yml')

db.init_app(app)

# Cria Tabelas
with app.app_context():
    db.create_all()

# Rotas Alunos
app.add_url_rule("/alunos", view_func=AlunoController.listar_alunos, methods=["GET"])
app.add_url_rule("/alunos/<int:aluno_id>", view_func=AlunoController.exibir_aluno, methods=["GET"])
app.add_url_rule("/alunos", view_func=AlunoController.criar_aluno, methods=["POST"])
app.add_url_rule("/alunos/<int:aluno_id>", view_func=AlunoController.atualizar_aluno, methods=["PUT"])
app.add_url_rule("/alunos/<int:aluno_id>", view_func=AlunoController.deletar_aluno, methods=["DELETE"])

# Rotas Professores
app.add_url_rule("/professores", view_func=ProfessorController.listar_professores, methods=["GET"])
app.add_url_rule("/professores/<int:professor_id>", view_func=ProfessorController.exibir_professor, methods=["GET"])
app.add_url_rule("/professores", view_func=ProfessorController.criar_professor, methods=["POST"])
app.add_url_rule("/professores/<int:professor_id>", view_func=ProfessorController.atualizar_professor, methods=["PUT"])
app.add_url_rule("/professores/<int:professor_id>", view_func=ProfessorController.deletar_professor, methods=["DELETE"])

# Rotas Turmas
app.add_url_rule("/turmas", view_func=TurmaController.listar_turmas, methods=["GET"])
app.add_url_rule("/turmas/<int:turma_id>", view_func=TurmaController.exibir_turma, methods=["GET"])
app.add_url_rule("/turmas", view_func=TurmaController.criar_turma, methods=["POST"])
app.add_url_rule("/turmas/<int:turma_id>", view_func=TurmaController.atualizar_turma, methods=["PUT"])
app.add_url_rule("/turmas/<int:turma_id>", view_func=TurmaController.deletar_turma, methods=["DELETE"])


if __name__ == '__main__':
    app.run(debug=True, port=5000)