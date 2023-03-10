from flask_restx import Resource, Namespace
from flask import request

from service_container import movie_service
from dao.models.movie import MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        status = request.args.get('status')
        page = request.args.get('page')

        return movies_schema.dump(movie_service.get_all(page, status)), 200


@movie_ns.route('/<int:pk>')
class MovieView(Resource):
    def get(self, pk):
        return movie_schema.dump(movie_service.get_one(pk=pk)), 200
