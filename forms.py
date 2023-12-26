from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class RegistraForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20 )] )
    password