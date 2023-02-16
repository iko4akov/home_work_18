from dao.model.genres import Genre


class GenreDAO():
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.get_one(gid)


    def get_all(self):
        return self.session.query(Genre).all()


    def create(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre):

        self.session.add(genre)
        self.session.commit()

        return genre


    def delete(self, gid):
        author = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
