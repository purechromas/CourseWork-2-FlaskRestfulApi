import jwt
from flask import request, abort

from constants import TOKEN_SECRET, TOKEN_ALGORITHM


def auth_required(func):
    def wrapped(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, key=TOKEN_SECRET, algorithms=[TOKEN_ALGORITHM])
        except Exception as e:
            print('JWT Decode exception', e)

        return func(*args, **kwargs)
    return wrapped
