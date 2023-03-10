from dao.models.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def create(self, favorite):
        new_director = Favorite(**favorite)

        self.session.add(new_director)
        self.session.commit()

    def delete(self, pk):
        favorite = self.session.query(Favorite).get(pk)

        self.session.delete(favorite)
        self.session.commit()
