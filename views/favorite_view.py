from flask_restx import Resource, Namespace
from flask import request

from service_container import favorite_service
from dao.models.favorite import FavoriteSchema

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies/<int:pk>')
class FavoriteView(Resource):
    def post(self, pk):
        user_id = request.json.get('user_id')

        favorite_service.create(user_id, pk)

        return '', 204

    def delete(self, pk):
        favorite_service.delete(pk)
