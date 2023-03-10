import base64
import hashlib
import hmac
from flask import abort

from dao.models.user import UserSchema
from dao.user_dao import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

user_schema = UserSchema()

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user):
        user['password'] = self.encode_password(user.get('password'))

        return self.dao.create(user)

    def update(self, pk, user):
        db_user = self.dao.get_one(pk)
        password = user.get('password')
        new_password = user.get('new_password')
        db_user_password = db_user.password

        compare = self.compare_passwords(db_user_password, password)

        if not compare:
            return abort(400)

        db_user.password = self.encode_password(new_password)

        return self.dao.update(db_user)

    def update_partial(self, pk, user):
        update_user = self.dao.get_one(pk)

        if 'name' in user:
            update_user.name = user.get('name')
        if 'surname' in user:
            update_user.surname = user.get('surname')
        if 'favorite_genre' in user:
            update_user.favorite_genre = user.get('favorite_genre')

        return self.dao.update(update_user)

    def delete(self, pk):
        return self.dao.delete(pk)

    def encode_password(self, password):
        new_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(new_password)

    def compare_passwords(self, password_db, password) -> bool:
        new_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        decode_db_password = base64.b64decode(password_db)

        return hmac.compare_digest(decode_db_password, new_password)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)
