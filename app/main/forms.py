from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField, DateTimeField
# from .forms import UpdateProfile
from .. import db
from wtforms.validators import InputRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content= TextAreaField('Pitch', validators=[InputRequired()])
    category= SelectField('Category', choices=[('Product','Product'), ('Pick-Up Lines'),('Pick-Up Lines'), ('Business','Business'), ('Other','Other')], validators=[InputRequired()])
    time= DateTimeField()
