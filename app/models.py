from . import db

class User(db.Model):
    __tablename__ = 'users'
    id =db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    bio = db.Column(db.Text())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id =db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    content = db.Column(db.Text())

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()