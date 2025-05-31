from flask import request, redirect, url_for, render_template
from . import task_bp
from ..models import User, Task, db
from flask_login import login_required, current_user


@task_bp.route('/', methods=['GET', 'POST'])
@login_required
def task():
        
    if request.method== 'POST':
        title = request.form['titleForm']
        description = request.form['descForm']
        user_id = current_user.id

        newtask = Task(title=title, description=description, user_id=user_id)

        db.session.add(newtask)
        db.session.commit()

    usertasks = Task.query.filter_by(user_id=current_user.id)

    return render_template('task.html', usertasks=usertasks)

@task_bp.route('/remove_task/<int:id>', methods=['POST'])
def remove_task(id):
    task= Task.query.filter_by(id=id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('task.task'))
        