from flask import Blueprint, render_template, request, redirect, url_for
from models.teacher import Teacher
from models.discipline import Discipline

teacher_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

@teacher_bp.route('/')
def index():
    teachers = Teacher.get_all()
    return render_template('teachers/index.html', teachers=teachers)

@teacher_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        user = request.form['user']
        password = request.form['password']
        Teacher.create(name, phone, user, password)
        return redirect(url_for('teachers.index'))
    return render_template('teachers/create.html')

@teacher_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    teacher = Teacher.get_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        user = request.form['user']
        password = request.form['password']
        Teacher.update(id, name, phone, user, password)
        return redirect(url_for('teachers.index'))
    return render_template('teachers/edit.html', teachers=teacher['teacher'])

@teacher_bp.route('/<int:id>/disciplines', methods=['GET', 'POST'])
def disciplinas(id):
    teacher = Teacher.get_by_id(id)
    all_disciplines = Discipline.get_all()
    if request.method == 'POST':
        discipline_ids = request.form.getlist('disciplines')
        Teacher.update_discipline(id, discipline_ids)
        return redirect(url_for('teachers.index'))
    return render_template(
        'teachers/disciplines.html',
        teacher=teacher,
        all_disciplines=all_disciplines
    )

@teacher_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    Teacher.delete(id)
    return redirect(url_for('teachers.index'))
