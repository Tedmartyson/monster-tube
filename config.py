import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/<database>'
SQLALCHEMY_TRACK_MODIFICATIONS = False