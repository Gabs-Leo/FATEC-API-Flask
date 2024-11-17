from flask import Blueprint, render_template, request, redirect, url_for
from models.discipline import Discipline

discipline_bp = Blueprint('disciplines', __name__, url_prefix='/disciplines')

@discipline_bp.route('/')
def index():
    disciplines = Discipline.get_all()
    return render_template('disciplines/index.html', disciplines=disciplines)

@discipline_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        hours = request.form['hours']
        Discipline.create(name, hours)
        return redirect(url_for('disciplines.index'))
    return render_template('disciplines/create.html')

@discipline_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    discipline = Discipline.get_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        hours = request.form['hours']
        Discipline.update(id, name, hours)
        return redirect(url_for('disciplines.index'))
    return render_template('disciplines/edit.html', discipline=discipline)

@discipline_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    Discipline.delete(id)
    return redirect(url_for('disciplines.index'))
