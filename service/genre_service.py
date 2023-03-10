from dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self, page=None):
        return self.dao.get_all(page)

    def create(self, genre):
        self.dao.create(genre)

    def update(self, pk, genre):
        update_genre = self.get_one(pk)
        update_genre.name = genre.get('name')
        self.dao.update(update_genre)

    def delete(self, pk):
        self.dao.delete(pk)
