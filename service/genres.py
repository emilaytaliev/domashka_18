from dao.genres import GenreDAO


class GenreService:
    def __init__(self, genres_dao: GenreDAO):
        self.genres_dao = genres_dao

    def get_all(self):
        return self.genres_dao.get_all()


    def get_one(self, id):
        return self.genres_dao.get_one(id)