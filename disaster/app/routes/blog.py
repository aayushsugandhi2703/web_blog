from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import PostForm
from app.models import PostData, Session

post = Blueprint('post', __name__, template_folder='templates', static_folder='static')

@post.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        try:
            session = Session()
            new_post = PostData(
                title=form.title.data,
                content=form.content.data,
                user_id=current_user.id
            )
            session.add(new_post)
            session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('main.home'))
        except:
            session.rollback()
            flash('An error occurred. Please try again', 'danger')
        finally:
            session.close()
    return render_template('create_post.html', title='Create Post', form=form)

@post.route('/posts')
def posts():
    session = Session()
    posts = session.query(PostData).all()
    session.close()
    return render_template('index.html', posts=posts)
