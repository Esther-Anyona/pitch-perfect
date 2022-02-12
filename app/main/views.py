from flask import render_template, redirect, url_for, request, abort
from . import main
from ..models import User, Pitch
from .forms import UpdateProfile, PitchForm
from flask_login import login_required
from .. import db,photos


@main.route('/')
def home():
    pitches = Pitch.query.all()
    return render_template('home.html', pitches=pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.get_pitch(user.id)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitches=pitches)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch/new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch= Pitch(title = form.title.data, content = form.content.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.home'))
        
    return render_template('pitch.html', form = form)