# from app.models import User
from app import create_app, db
from flask.cli import FlaskGroup
from flask_migrate import Migrate

migrate = Migrate()

# Creating app instance
app = create_app('production')
cli = FlaskGroup(app)

migrate.init_app(app, db)


@cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    cli()
