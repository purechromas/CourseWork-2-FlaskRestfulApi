from dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self, page=None):
        return self.dao.get_all(page)

    def create(self, director):
        self.dao.create(director)

    def update(self, pk, director):
        update_director = self.get_one(pk)
        update_director.name = director.get('name')
        self.dao.update(update_director)

    def delete(self, pk):
        self.dao.delete(pk)
