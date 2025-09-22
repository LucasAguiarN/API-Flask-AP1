from models import db


# Class que vira uma Tabela no Banco de Dados
class Aluno(db.Model):

    # Nome da Tabela
    __tablename__ = 'aluno'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nasc = db.Column(db.Float, nullable=False)
    nota_1semestre = db.Column(db.Float, nullable=False)
    nota_2semestre = db.Column(db.Float, nullable=False)
    media = db.Column(db.Float, nullable=False)

    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)

    # Relacionamento Muitos-para-Um (N:1) com Tabela Turma
    turma = db.relationship("Turma", back_populates="alunos")

    def __repr__(self):
        return f"<Aluno {self.nome} ID: {self.id}>"