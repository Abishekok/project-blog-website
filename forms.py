from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SearchField, BooleanField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistraForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20 )] )
    email = StringField('Email', validators=[DataRequired(), Email()] )
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')




class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()] )
  password = PasswordField('password', validators=[DataRequired()])
  rememeber = BooleanField('Remenmber Me')
  submit = SubmitField('Login')
    