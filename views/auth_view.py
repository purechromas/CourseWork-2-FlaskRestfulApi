from flask_restx import Resource, Namespace
from flask import request

from service_container import user_service
from service_container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegisterService(Resource):
    def post(self):
        user = request.json

        user_service.create(user)


@auth_ns.route('/login')
class AuthLoginService(Resource):
    def post(self):
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            return '', 400

        tokens = auth_service.generate_token(email, password)

        return tokens

    def put(self):
        data = request.json

        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
