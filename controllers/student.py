from flask import Blueprint, render_template, request, redirect, url_for
from models.student import Student
from models.course import Course

aluno_bp = Blueprint('alunos', __name__, url_prefix='/alunos')

@aluno_bp.route('/')
def index():
    alunos = Aluno.get_all()
    return render_template('alunos/index.html', alunos=alunos)

@aluno_bp.route('/create', methods=['GET', 'POST'])
def create():
    cursos = Curso.get_all()
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        senha = request.form['senha']
        curso_id = request.form['curso_id'] if 'curso_id' in request.form else None
        Aluno.create(nome, cpf, endereco, senha, curso_id)
        return redirect(url_for('alunos.index'))
    return render_template('alunos/create.html', cursos=cursos)

@aluno_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    aluno = Aluno.get_by_id(id)
    cursos = Curso.get_all()
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        senha = request.form['senha']
        curso_id = request.form['curso_id'] if 'curso_id' in request.form else None
        Aluno.update(id, nome, cpf, endereco, senha, curso_id)
        return redirect(url_for('alunos.index'))
    return render_template('alunos/edit.html', aluno=aluno, cursos=cursos)

@aluno_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    Aluno.delete(id)
    return redirect(url_for('alunos.index'))
