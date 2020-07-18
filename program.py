from flask import Flask, render_template
from extentions import bootstrap, db, login_manager, migrate
from login import blueprint
import models


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.settings')
    app.register_blueprint(blueprint)
    init_extentions(app)
    return app


def init_extentions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login.login'
    migrate.init_app(app, db)


def main():
    app = create_app()
    app.run(port=9000, debug=True)


if __name__ == '__main__':
    main()
