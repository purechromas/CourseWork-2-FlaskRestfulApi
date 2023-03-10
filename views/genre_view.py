from flask_restx import Resource, Namespace
from flask import request

from service_container import genre_service
from dao.models.genre import GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('')
class GenresView(Resource):
    def get(self):
        page = request.args.get('page')

        return genres_schema.dump(genre_service.get_all(page))


@genre_ns.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        return genre_schema.dump(genre_service.get_one(pk))
