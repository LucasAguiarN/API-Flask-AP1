from flask import jsonify, request
from models import db
from models.professor import Professor
from models.turma import Turma


class TurmaController:
    
    @staticmethod
    def listar_turmas():
        turmas = Turma.query.all()
        if turmas:
            lista = []
            for turma in turmas:
                lista.append(turma.para_dicionario())
            return jsonify(lista), 200
        else:
            mensagem = {"Erro": "Lista de Turmas Vazia!"}
            return jsonify(mensagem), 200
        
    @staticmethod
    def exibir_turma(turma_id):
        turma = Turma.query.get(turma_id)
        if turma:
            return jsonify(turma.para_dicionario()), 200
        else:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 200
    
    @staticmethod
    def criar_turma():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        descricao = dados.get("descricao")
        ativo = True if dados.get("ativo") == "True" else False
        professor_id = dados.get("professor_id")

        registro_turma = Turma.query.filter_by(descricao=descricao).first()
        if registro_turma:
            mensagem = {"Erro": "Turma Já Cadastrado!"}
            return jsonify(mensagem), 200
        
        registro_professor = Professor.query.filter_by(id=professor_id).first()
        if not registro_professor:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 200

        nova_turma = Turma(
            descricao = descricao,
            ativo = ativo, 
            professor_id = professor_id
        )

        db.session.add(nova_turma)
        db.session.commit()

        mensagem = {"Mensagem": "Turma Cadastrada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def atualizar_turma(turma_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        turma = Turma.query.get(turma_id)
        if turma is None:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 200
        
        descricao = dados.get("descricao")
        ativo = True if dados.get("ativo") == "True" else False
        professor_id = dados.get("professor_id")
      
        registro_professor = Professor.query.filter_by(id=professor_id).first()
        if not registro_professor:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 200

        turma.descricao = descricao
        turma.ativo = ativo
        turma.professor_id = professor_id

        db.session.commit()
        
        mensagem = {"Mensagem": "Turma Atualizada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def deletar_turma(turma_id):

        turma = Turma.query.get(turma_id)
        if turma is None:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 200
        
        if turma.alunos:
           return jsonify({"Erro": "Turma com Aluno Vinculado!"}), 400
        
        db.session.delete(turma)
        db.session.commit()
        
        mensagem = {"Mensagem": "Turma Deletada com Sucesso!"}
        return jsonify(mensagem), 201