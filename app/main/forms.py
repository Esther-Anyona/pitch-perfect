from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField, DateTimeField, RadioField
from .. import db
from wtforms.validators import InputRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content= TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Post Pitch')

class CommentForm(FlaskForm):
	comment = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()