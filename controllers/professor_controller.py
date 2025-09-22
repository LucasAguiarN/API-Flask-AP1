from flask import render_template, request
from models import db
from models.professor import Professor
from models.turma import Turma


class ProfessorController:
    return