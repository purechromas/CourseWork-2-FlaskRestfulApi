import unittest
from unittest.mock import MagicMock
from service.user_service import UserService
from dao.user_dao import UserDAO


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.u1 = {'email': 'purechromas@gmail.com', 'password': 'godmode'}
        self.u2 = {'email': 'kudashkinaolga@gmail.com', 'password': 'trymypassword'}
        self.u3 = {'email': 'onemoregame@gmail.com', 'password': 'unreal'}

        self.dao = UserDAO(None)
        self.user_service = UserService(dao=self.dao)

        self.user_service.get_one = MagicMock(return_value=self.u1)
        self.user_service.get_all = MagicMock(return_value=[self.u1, self.u2, self.u3])
        self.user_service.create = MagicMock(return_value=self.u2)
        self.user_service.update = MagicMock(return_value=self.u2)
        self.user_service.delete = MagicMock(return_value=True)

    def test_encode_password(self):
        self.password = 'deathfact0r'
        self.db_password = self.user_service.encode_password(self.password)

        assert self.db_password is not None

    def test_compare_password(self):
        self.compare_password = 'trythisout'
        self.db_password = self.user_service.encode_password(self.compare_password)
        test = self.user_service.compare_passwords(self.db_password, self.compare_password)
        self.assertTrue(test)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user['email'] == 'purechromas@gmail.com'
        assert user['password'] == 'godmode'

    def test_get_all(self):
        users = self.user_service.get_all()

        assert users is not None
        assert len(users) > 1
        assert len(users) == 3
        assert users[0]['password'] == 'godmode'

    def test_create_all(self):
        user = self.user_service.create(self.u2)

        assert user is not None
        assert user['email'] == 'kudashkinaolga@gmail.com'
        assert user['password'] == 'trymypassword'

    def test_update(self):
        self.u2['password'] = 'itiq300'
        user = self.user_service.update(self.u2)

        assert user is not None
        assert user['password'] == 'itiq300'

    def test_delete(self):
        result = self.user_service.delete(self.u1)

        self.assertTrue(result)
