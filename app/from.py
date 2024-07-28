from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class loignform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class signupform(FlaskForm):
    name = StringField('nmae', validators=[DataRequired(), Length( max=20)])
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class postform(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=50)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')