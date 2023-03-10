from flask import Flask
from flask_restx import Api

from database import db
from configuration import Config
from views.movie_view import movie_ns
from views.genre_view import genre_ns
from views.director_view import director_ns
from views.auth_view import auth_ns
from views.user_view import user_ns

application = Flask(__name__)


def extend_application(app):
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    extend_application(application)
    application.run()
