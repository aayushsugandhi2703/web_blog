from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, LoginManager
from app.forms import LoginForm, SignupForm
from app.models import UserData, Session

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(UserData).get(user_id)
    session.close()
    return user

def init_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = Session()
        user = session.query(UserData).filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
        session.close()
    return render_template('login.html', title='Login', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            session = Session()
            user = UserData(
                name=form.name.data,
                username=form.username.data,
                password=form.password.data  # Storing plain text password (not recommended)
            )
            session.add(user)
            session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('auth.login'))
        except:
            session.rollback()
            flash('An error occurred. Please try again', 'danger')
        finally:
            session.close()
    return render_template('signup.html', title='Sign Up', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
