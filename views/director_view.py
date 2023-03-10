from flask_restx import Resource, Namespace
from flask import request

from service_container import director_service
from dao.models.director import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('')
class DirectorsView(Resource):
    def get(self):
        page = request.args.get('page')

        return directors_schema.dump(director_service.get_all(page))


@director_ns.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        return director_schema.dump(director_service.get_one(pk))
