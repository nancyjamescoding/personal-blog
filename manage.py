# from app.models import User
from app import create_app
from flask.cli import FlaskGroup


# Creating app instance
app = create_app('development')
cli = FlaskGroup(app)
if __name__ == '__main__':
    cli()
