from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200),unique=True)
    username=db.Column(db.String(200),unique=True)
    password_hash = db.Column(db.String(200))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Posts(db.Model):
    __tablename__='posts'

    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(200))
    content = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_post(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}'

class Comments(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer, primary_key=True)
    comment= db.Column(db.String(200))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    posts_id = db.Column(db.Integer,db.ForeignKey("posts.id"))

    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    def __repr__(self):
        return f'User {self.username}'
