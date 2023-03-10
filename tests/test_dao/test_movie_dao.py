import unittest
from unittest.mock import MagicMock
from dao.movie_dao import MovieDAO


class TestMovieDAO(unittest.TestCase):
    def setUp(self):
        self.m1 = {'title': 'Йеллоустоун', 'year': 2018}
        self.m2 = {'title': 'Чикаго', 'year': 2002}
        self.m3 = {'title': 'Одержимость', 'year': 2013}

        self.dao = MovieDAO(None)
        self.dao.get_one = MagicMock(return_value=self.m1)
        self.dao.get_all = MagicMock(return_value=[self.m1, self.m2, self.m3])
        self.dao.create = MagicMock(return_value=self.m2)
        self.dao.update = MagicMock(return_value=self.m2)
        self.dao.delete = MagicMock(return_value=True)

    def test_get_one(self):
        movie = self.dao.get_one(1)

        assert movie is not None
        assert movie['title'] == 'Йеллоустоун'
        assert movie['year'] == 2018

    def test_get_all(self):
        movies = self.dao.get_all()

        assert movies is not None
        assert len(movies) > 1
        assert len(movies) == 3
        assert movies[0]['title'] == 'Йеллоустоун'

    def test_create_all(self):
        movie = self.dao.create({'title': 'Чикаго', 'year': 2002})

        assert movie is not None
        assert movie['title'] == 'Чикаго'
        assert movie['year'] == 2002

    def test_update(self):
        self.m2['title'] = 'Spiderman'
        movie = self.dao.update(self.m2)

        assert movie is not None
        assert movie['title'] == 'Spiderman'

    def test_delete(self):
        result = self.dao.delete(self.m1)

        self.assertTrue(result)