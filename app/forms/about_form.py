from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AboutForm(FlaskForm):
    about = StringField('about', validators=[DataRequired()])