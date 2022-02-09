from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from .forms import ReviewForm,UpdateProfile
from .. import db
from wtforms.validators import InputRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')