from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_mail import Mail,Message

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view ='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
admin = Admin()
mail = Mail()


def create_app(config_state):
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])


    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    admin.init_app(app)
    mail.init_app(app)



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')


    return app
