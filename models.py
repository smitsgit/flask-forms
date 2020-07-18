from extentions import db
from flask_login import UserMixin
from extentions import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def user_loader(id: int):
    return User.query.get(id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
