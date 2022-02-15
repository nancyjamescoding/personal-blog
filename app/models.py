# from app import create_app
# from flask_script import Manager, Server
# from . import db


# # ßCreating app instance
# app = create_app('development')

# manager = Manager(app)
# manager.add_command('server', Server)


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(255))

#     def __repr__(self):
#         return f'User {self.username}'


# @manager.shell
# def make_shell_context():
#     return dict(app=app, db=db, User=User)


# if __name__ == '__main__':
#     manager.run()

# # ....


# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User', backref='role', lazy="dynamic")

#     def __repr__(self):
#         return f'User {self.name}'
