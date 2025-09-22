from flask import render_template, request
from models import db
from models.aluno import Aluno
from models.turma import Turma


class AlunoController:
    return