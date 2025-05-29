from flask import request, redirect, url_for, render_template
from . import task_bp
from ..models import User, Task, db
from flask_login import login_required

@login_required
@task_bp.route('/task', methods=['GET', 'POST'])
def task():
    if request.method== 'GET':
        return render_template('dashboard.html')