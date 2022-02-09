from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
# from .forms import UpdateProfile
from .. import db
from wtforms.validators import InputRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Save')