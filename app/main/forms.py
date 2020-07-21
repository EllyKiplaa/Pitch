 
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from ..models import Pitch, Comment
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Pitch Category Title', validators=[DataRequired()])
    pitch = TextAreaField('YOUR PITCH',validators=[DataRequired()])
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment here',validators=[DataRequired()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    name =  StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Create')