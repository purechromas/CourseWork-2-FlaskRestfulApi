from dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Director).get(pk)

    def get_all(self, page):
        if page:
            return self.session.query(Director).paginate(per_page=12)
        else:
            return self.session.query(Director).all()

    def create(self, director):
        new_director = Director(**director)

        self.session.add(new_director)
        self.session.commit()

    def update(self, director):
        self.session.add(director)
        self.session.commit()

    def delete(self, pk):
        director = self.get_one(pk)

        self.session.delete(director)
        self.session.commit()
