from flask_restx import Resource, Namespace
from flask import request

from service_container import user_service
from dao.models.user import UserSchema
from decorators import auth_required

user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/<int:pk>')
class UserView(Resource):
    @auth_required
    def get(self, pk):
        return user_schema.dump(user_service.get_one(pk))

    @auth_required
    def patch(self, pk):
        user = request.json
        user_service.update_partial(pk, user)

        return '', 401

    @auth_required
    def put(self, pk):
        data = request.json

        password = data.get('password', None)
        new_password = data.get('new_password', None)

        if password is None:
            return 'write your password', 400

        if new_password is None:
            return 'write your new password', 400

        if len(new_password) < 6:
            return 'your new password is too short', 400

        user_service.update(pk, data)

        return '', 204
