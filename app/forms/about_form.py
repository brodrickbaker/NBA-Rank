from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from app.models import User


class AboutForm(FlaskForm):
    about = StringField('about', validators=[DataRequired()])