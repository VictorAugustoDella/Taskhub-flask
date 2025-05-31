from flask import request, redirect, render_template, url_for
from . import auth_bp
from flask_login import login_user, logout_user, login_required
from ..models import User, Task, db




@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        error=False
        return render_template('login.html')
    else:
        username= request.form['usernameForm']
        password= request.form['passwordForm']

        userquery= User.query.filter_by(username=username, password=password).first()

        if userquery:
            
            login_user(userquery)
            return redirect(url_for('task.task'))
        else:
            return render_template('login.html', erro=True)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        username= request.form['usernameForm']
        password= request.form['passwordForm']

        userquery= User.query.filter_by(username=username).first()

        if userquery:
            return render_template('register.html', erro=True)
        else:
            useradd = User(username=username, password=password)
            db.session.add(useradd)
            db.session.commit()
            login_user(useradd)

            return redirect(url_for('auth.login'))


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))