from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    Title = StringField('Title', validators = [DataRequired(), Length(min=1, max=20)])
    Description = TextAreaField('description', validators =[ DataRequired(), Length (min =1, max=100)])
    Submit = SubmitField('Create Task')