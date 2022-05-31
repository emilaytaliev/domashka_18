from dao.movies import MovieDAO


class MovieService:
    def __init__(self, movies_dao: MovieDAO):
        self.movies_dao = movies_dao

    def get_all(self):
        return self.movies_dao.get_all()

    def create(self, data):
        self.movies_dao.create(data)

    def get_one(self, id):
        return self.movies_dao.get_one(id)

    def update(self, data, id):
        movie = self.movies_dao.get_one(id)
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        self.movies_dao.update(movie)

    def delete(self, id):
        movie = self.movies_dao.get_one(id)
        self.movies_dao.delete(movie)

    def get_be_years(self, id):
        return self.movies_dao.get_years(id)

    def get_be_directors(self, id):
        return self.movies_dao.get_directors(id)

    def get_be_genre(self, id):
        return self.movies_dao.get_genres(id)





