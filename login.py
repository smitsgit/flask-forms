from flask import Blueprint, render_template

from forms import LoginForm

blueprint = Blueprint('login', __name__)


@blueprint.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "Hello World"
    return render_template('login.html', form=form)
