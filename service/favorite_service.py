from dao.favorite_dao import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def create(self, user_id, movie_id):
        data = {
            'user_id': user_id,
            'movie_id': movie_id
        }

        self.dao.create(data)

    def delete(self, pk):
        self.dao.delete(pk)
