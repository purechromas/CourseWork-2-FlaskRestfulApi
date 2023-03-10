from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self, page=None, status=None):
        return self.dao.get_all(page, status)

    def get_new_movie(self, page_number=None):
        return self.dao.get_new_movies(page_number=page_number)

    def create(self, movie):
        self.dao.create(movie)

    def update(self, pk, genre):
        update_movie = self.get_one(pk)
        update_movie.name = genre.get('name')
        self.dao.update(update_movie)

    def delete(self, pk):
        self.dao.delete(pk)
