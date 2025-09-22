from models import db


# Class que vira uma Tabela no Banco de Dados
class Professor(db.Model):

    # Nome da Tabela
    __tablename__ = 'professores'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    # Relacionamento Um-para-Muitos (1-N) com Tabela Turma
    turmas = db.relationship("Turma", back_populates="professor")

    def __repr__(self):
        return f"<Professor {self.nome} ID: {self.id}>"