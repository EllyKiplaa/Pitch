from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import Required


    
class signUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')