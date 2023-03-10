import json
from dao.models.director import Director
from dao.models.genre import Genre
from dao.models.user import User
from dao.models.movie import Movie
from dao.models.favorite import Favorite
from app import application
from configuration import Config
from database import db

with open('data.json', 'r', encoding='utf-8') as file:
    course_data = json.load(file)

with application.app_context():
    application.config.from_object(Config)
    db.init_app(application)
    db.create_all()

movies = course_data['movies']
directors = course_data['directors']
genres = course_data['genres']

for genre in genres:
    genre['id'] = genre.pop('pk')
    with application.app_context():
        db.session.add(Genre(**genre))
        db.session.commit()

for director in directors:
    director['id'] = director.pop('pk')
    with application.app_context():
        db.session.add(Director(**director))
        db.session.commit()

for movie in movies:
    movie['id'] = movie.pop('pk')
    with application.app_context():
        db.session.add(Movie(**movie))
        db.session.commit()

models = [Director, Genre, User, Movie, Favorite]
