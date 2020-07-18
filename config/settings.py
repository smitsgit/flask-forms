import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = 'whatthehell'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False