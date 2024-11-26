from flask import Blueprint, render_template, request, redirect, url_for
from models.student import Student
from models.course import Course

student_bp = Blueprint('students', __name__, url_prefix='/students')

@student_bp.route('/')
def index():
    students = Student.get_all()
    return render_template('students/index.html', students=students)

@student_bp.route('/create', methods=['GET', 'POST'])
def create():
    courses = Course.get_all()
    if request.method == 'POST':
        name = request.form['name']
        cpf = request.form['cpf']
        address = request.form['address']
        password = request.form['password']
        course_id = request.form['course_id'] if 'course_id' in request.form else None
        Student.create(name, cpf, address, password, course_id)
        return redirect(url_for('students.index'))
    return render_template('students/create.html', courses=courses)

@student_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    student = Student.get_by_id(id)
    courses = Course.get_all()
    if request.method == 'POST':
        name = request.form['name']
        cpf = request.form['cpf']
        address = request.form['address']
        password = request.form['password']
        course_id = request.form['course_id'] if 'course_id' in request.form else None
        Student.update(id, name, cpf, address, password, course_id)
        return redirect(url_for('students.index'))
    return render_template('students/edit.html', student=student, courses=courses)

@student_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    Student.delete(id)
    return redirect(url_for('students.index'))
