from dao.model.movies import Movie, MovieSchema


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movie.query.all()
        result = MovieSchema(many=True).dump(movies)
        return result

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def get_one(self, id):
        movie = Movie.query.get(id)
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()


    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

    def get_years(self, years):
        movie = Movie.query.filter(Movie.year == years)
        return movie

    def get_genres(self, genre_id):
        movie = Movie.query.filter(Movie.genre_id == genre_id)
        return movie

    def get_directors(self, director_id):
        movie = Movie.query.filter(Movie.director_id == director_id)
        return movie


