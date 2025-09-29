from flask import jsonify, request
from app import app
from models import db
from models.professor import Professor


class ProfessorController:
    
    @staticmethod
    @app.route('/professores', methods=['GET'])
    def listar_professores():
        professores = Professor.query.all()
        if not professores:
            return jsonify(professores), 200
        else:
            mensagem = {"Erro": "Lista de Professores Vazia!"}
            return jsonify(mensagem), 200
    
    @staticmethod
    @app.route('/professores', methods=['POST'])
    def criar_professor():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nome = dados.get("nome")
        idade = dados.get("idade")
        materia = dados.get("materia")
        observacoes = dados.get("observacoes")

        registro_professor = Professor.query.filter_by(nome=nome).first()
        if registro_professor:
            mensagem = {"Erro": "Professor Já Cadastrado!"}
            return jsonify(mensagem), 200

        novo_professor = Professor(
            nome = nome,
            idade = idade, 
            materia = materia,
            observacoes = observacoes
        )

        db.session.add(novo_professor)
        db.session.commit()

        mensagem = {"Mensagem": "Turma Cadastrada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    @app.route('/professores/<int:professor_id>', methods=['PUT'])
    def atualizar_professor(professor_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        professor = Professor.query.get(professor_id)
        if professor is None:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 200
        
        nome = dados.get("nome")
        idade = dados.get("idade")
        materia = dados.get("materia")
        observacoes = dados.get("observacoes")
      
        professor.nome = nome
        professor.idade = idade 
        professor.materia = materia
        professor.observacoes = observacoes

        db.session.commit()
        
        mensagem = {"Mensagem": "Professor Atualizado com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    @app.route('/professores/<int:professor_id>', methods=['DELETE'])
    def deletar_professor(professor_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        professor = Professor.query.get(professor_id)
        if professor is None:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 200
        
        db.session.delete(professor)
        db.session.commit()
        
        mensagem = {"Mensagem": "Professor Deletado com Sucesso!"}
        return jsonify(mensagem), 201