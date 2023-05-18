import logging
import os

from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from flask_appbuilder.security.manager import AUTH_DB

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# App secret key
app.secret_key = 'Secret_#@!@@KEY098$$_Key#IMBD_##$movies$###'

# The SQLAlchemy connection string.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://movieusers:movieworld@localhost:5432/movies'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['AUTH_TYPE'] = AUTH_DB
app.config['AUTH_USER_REGISTRATION'] = True
app.config['AUTH_USER_REGISTRATION_ROLE'] = 'Admin'
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_object("config")

db = SQLA(app)

appbuilder = AppBuilder(app, db.session)
from app.views import InsertMovies, MovieView
appbuilder.add_view(MovieView, "List Groups", category = "Movie detail list")
appbuilder.add_view(InsertMovies(), "Upload Movies", category="Upload Movies")
