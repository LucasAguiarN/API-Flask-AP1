from flask import jsonify, request
from models import db
from models.professor import Professor


class ProfessorController:
    
    @staticmethod
    def listar_professores():
        """
        Lista todos os professores cadastrados no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de professores e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        
        professores = Professor.query.all()
        if professores:
            lista = []
            for professor in professores:
                lista.append(professor.para_dicionario())
            return jsonify(lista), 200
        else:
            mensagem = {"Erro": "Lista de Professores Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_professor(professor_id):
        professor = Professor.query.get(professor_id)
        if professor:
            return jsonify(professor.para_dicionario()), 200
        else:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 404
    
    @staticmethod
    def criar_professor():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nome = dados.get("nome")
        idade = dados.get("idade")
        materia = dados.get("materia")
        observacoes = dados.get("observacoes")

        if (nome == None or idade == None or materia == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400

        registro_professor = Professor.query.filter_by(nome=nome).first()
        if registro_professor:
            mensagem = {"Erro": "Professor Já Cadastrado!"}
            return jsonify(mensagem), 409

        novo_professor = Professor(
            nome = nome,
            idade = idade, 
            materia = materia,
            observacoes = observacoes
        )

        db.session.add(novo_professor)
        db.session.commit()

        mensagem = {"Mensagem": "Professor Cadastrado com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def atualizar_professor(professor_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        professor = Professor.query.get(professor_id)
        if professor is None:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        nome = dados.get("nome")
        idade = dados.get("idade")
        materia = dados.get("materia")
        observacoes = dados.get("observacoes")

        if (nome == None or idade == None or materia == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
      
        professor.nome = nome
        professor.idade = idade 
        professor.materia = materia
        professor.observacoes = observacoes

        db.session.commit()
        
        mensagem = {"Mensagem": "Professor Atualizado com Sucesso!"}
        return jsonify(mensagem), 200
    
    @staticmethod
    def deletar_professor(professor_id):

        professor = Professor.query.get(professor_id)
        if professor is None:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        if professor.turmas:
            return jsonify({"Erro": "Professor com Turma Vinculada!"}), 404
        
        db.session.delete(professor)
        db.session.commit()
        
        mensagem = {"Mensagem": "Professor Deletado com Sucesso!"}
        return jsonify(mensagem), 200