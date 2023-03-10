from dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(User).get(pk)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_by_name(self, name):
        return self.session.query(User).filter(User.name == name).first()

    def create(self, user):
        new_user = User(**user)

        self.session.add(new_user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def delete(self, pk):
        user = self.get_one(pk)

        self.session.delete(user)
        self.session.commit()
