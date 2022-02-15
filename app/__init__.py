
# from flask import Flask
# from ..config import DevConfig
# from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from .main.views import *
# # Initializing application
# app = Flask(__name__, instance_relative_config=True)

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)
from config import config_options
from flask_bootstrap import Bootstrap
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    # Initializing Flask Extensions
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    # bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    return app
