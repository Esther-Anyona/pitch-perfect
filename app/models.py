from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id =db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(70))
    email = db.Column(db.String(150), unique=True)
    bio = db.Column(db.Text())
    profile_pic_path = db.Column(db.String(50))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id =db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.Text())
    time = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(150))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod    
    def get_pitch (cls, id):
        pitches = Pitch.query.filter_by(user_id = id).all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.content}'


class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.comment}"