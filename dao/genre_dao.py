from dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Genre).get(pk)

    def get_all(self, page=None):
        if page:
            return self.session.query(Genre).paginate(per_page=12)
        else:
            return self.session.query(Genre).all()

    def create(self, genre):
        new_genre = Genre(**genre)

        self.session.add(new_genre)
        self.session.commit()

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete(self, pk):
        genre = self.get_one(pk)

        self.session.delete(genre)
        self.session.commit()
