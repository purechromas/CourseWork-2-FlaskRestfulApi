import calendar
import datetime
import jwt
from flask import abort

from constants import TOKEN_SECRET, TOKEN_ALGORITHM


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            'email': user.email
        }

        # access token:
        minute30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['expire'] = calendar.timegm(minute30.timetuple())
        access_token = jwt.encode(data, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)

        # refresh token:
        day = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        data['expire'] = calendar.timegm(day.timetuple())
        refresh_token = jwt.encode(data, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=TOKEN_SECRET, algorithms=[TOKEN_ALGORITHM])
        email = data.get('email')

        user = self.user_service.get_by_email(email)

        if user is None:
            abort(404)
        return self.generate_token(email, None, is_refresh=True)
