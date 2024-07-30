from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash
from app.models import Task, Session
from app.forms import TaskForm

task_bp = Blueprint('task_bp', __name__, template_folder='/templates')

@task_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('task_bp.display'))

@task_bp.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        session = Session()
        task = Task(Title=form.Title.data, Description=form.Description.data)
        session.add(task)
        session.commit()
        session.close()
        flash('Task added successfully')
        return redirect(url_for('task_bp.display'))
    return render_template('add_task.html', form=form)

@task_bp.route('/display', methods=['GET'])
def display():
    session = Session()
    tasks = session.query(Task).all()
    session.close()
    return render_template('display_tasks.html', tasks=tasks)

@task_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    session = Session()
    task = session.query(Task).get(int(id))
    if not task:
        flash('Task not found')
    else:
        session.delete(task)
        session.commit()
        flash('Task deleted successfully')
    session.close()
    
    return redirect(url_for('task_bp.display'))
