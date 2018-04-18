from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(60))
    email = db.Column(db.String(60),unique=True)
    username=db.Column(db.String(60),unique=True)
    password=db.Column(db.String(60),unique=True)

    def __repr__(self):
        return f'User {self.username}'
