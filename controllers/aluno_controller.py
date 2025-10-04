from flask import jsonify, request
from models import db
from models.aluno import Aluno
from models.turma import Turma
from datetime import datetime


class AlunoController:
    
    @staticmethod
    def listar_alunos():
        alunos = Aluno.query.all()
        if alunos:
            lista = []
            for aluno in alunos:
                lista.append(aluno.para_dicionario())
            return jsonify(lista), 200
        else:
            mensagem = {"Erro": "Lista de Alunos Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_aluno(aluno_id):
        aluno = Aluno.query.get(aluno_id)
        if aluno:
            return jsonify(aluno.para_dicionario()), 200
        else:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404
    
    @staticmethod
    def criar_aluno():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nome = dados.get("nome")
        idade = dados.get("idade")
        data = dados.get("data_nasc")
        nota_1semestre = dados.get("nota_1semestre")
        nota_2semestre = dados.get("nota_2semestre")
        turma_id = dados.get("turma_id")

        if (nome == None or idade == None or data == None or nota_1semestre == None or nota_2semestre == None or turma_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        media =  (int(nota_1semestre) + int(nota_2semestre)) / 2
        data_nasc = datetime.strptime(data, "%d/%m/%Y").date()

        registro_alunos = Aluno.query.filter_by(nome=nome).first()
        if registro_alunos:
            mensagem = {"Erro": "Aluno Já Cadastrado!"}
            return jsonify(mensagem), 409
        
        registro_turmas = Turma.query.filter_by(id=turma_id).first()
        if not registro_turmas:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 404

        novo_aluno = Aluno(
            nome = nome,
            idade = idade, 
            data_nasc = data_nasc,
            nota_1semestre = nota_1semestre,
            nota_2semestre = nota_2semestre,
            media = media,
            turma_id = turma_id
        )

        db.session.add(novo_aluno)
        db.session.commit()

        mensagem = {"Mensagem": "Aluno Cadastrado com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def atualizar_aluno(aluno_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        aluno = Aluno.query.get(aluno_id)
        if aluno is None:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        nome = dados.get("nome")
        idade = dados.get("idade")
        data = dados.get("data_nasc")
        nota_1semestre = dados.get("nota_1semestre")
        nota_2semestre = dados.get("nota_2semestre")
        turma_id = dados.get("turma_id")

        if (nome == None or idade == None or data == None or nota_1semestre == None or nota_2semestre == None or turma_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        media =  (int(nota_1semestre) + int(nota_2semestre)) / 2
        data_nasc = datetime.strptime(data, "%d/%m/%Y").date()
      
        registro_turmas = Turma.query.filter_by(id=turma_id).first()
        if not registro_turmas:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 404

        aluno.nome = nome
        aluno.idade = idade 
        aluno.data_nasc = data_nasc
        aluno.nota_1semestre = nota_1semestre
        aluno.nota_2semestre = nota_2semestre
        aluno.media = media
        aluno.turma_id = turma_id

        db.session.commit()
        
        mensagem = {"Mensagem": "Aluno Atualizado com Sucesso!"}
        return jsonify(mensagem), 200
    
    @staticmethod
    def deletar_aluno(aluno_id):

        aluno = Aluno.query.get(aluno_id)
        if aluno is None:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        db.session.delete(aluno)
        db.session.commit()
        
        mensagem = {"Mensagem": "Aluno Deletado com Sucesso!"}
        return jsonify(mensagem), 200