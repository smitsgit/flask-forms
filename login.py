from flask import Blueprint, render_template, url_for, redirect, request
from forms import LoginForm
from flask_login import current_user, login_user, login_required, logout_user
from models import User

blueprint = Blueprint('login', __name__)


@blueprint.route("/home")
@login_required
def home():
    return "Hello World"


@blueprint.route("/")
def index():
    return "Index world"


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login.index'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("login.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for("login.index"))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=form)
