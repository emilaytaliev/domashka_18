from dao.model.genres import Genre, GenreSchema


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genre = Genre.query.all()
        result = GenreSchema(many=True).dump(genre)
        return result


    def get_one(self, id):
        genre = Genre.query.get(id)
        return genre
