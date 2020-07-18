from flask import Flask, render_template
from extentions import bootsrap
from login import blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.settings')
    app.register_blueprint(blueprint)
    init_extentions(app)
    return app


def init_extentions(app):
    bootsrap.init_app(app)


def main():
    app = create_app()
    app.run(port=9000, debug=True)


if __name__ == '__main__':
    main()
