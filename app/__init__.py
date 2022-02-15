
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
db = SQLAlchemy()

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
