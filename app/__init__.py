from flask import Flask
from flask_login import LoginManager
from app.models import db, User, Task
from app.auth import auth_bp
from app.task import task_bp

def create_app():
    app = Flask(__name__)
    app.secret_key='XERECA'
    lm= LoginManager(app)
    lm.login_view='login'

    @lm.user_loader
    def user_loader(id):
        usuario = db.session.query(User).filter_by(id=id).first()
        return usuario

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    with app.app_context():
        db.create_all()

    return app