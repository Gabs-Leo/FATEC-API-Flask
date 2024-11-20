from flask import Blueprint, render_template, request, redirect, url_for
from models.course import Course
from models.discipline import Discipline

course_bp = Blueprint('courses', __name__, url_prefix='/courses')

@course_bp.route('/')
def index():
    courses = Course.get_all()
    return render_template('courses/index.html', courses=courses)

@course_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        Course.create(name)
        return redirect(url_for('courses.index'))
    return render_template('courses/create.html')

@course_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    course = Course.get_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        Course.update(id, name)
        return redirect(url_for('courses.index'))
    return render_template('courses/edit.html', course=course)

@course_bp.route('/<int:id>/disciplines', methods=['GET', 'POST'])
def disciplines(id):
    course = Course.get_by_id(id)
    all_disciplines = Discipline.get_all()
    course_discipline_ids = [discipline['id'] for discipline in course['disciplines']]

    if request.method == 'POST':
        discipline_ids = request.form.getlist('disciplines')
        Course.update_disciplines(id, discipline_ids)
        return redirect(url_for('courses.index'))
    return render_template(
        'courses/disciplines.html',
        course=course,
        all_disciplines=all_disciplines,
        course_discipline_ids=course_discipline_ids
    )

@course_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    Course.delete(id)
    return redirect(url_for('courses.index'))
