from setup_db import db
from dao.movies import MovieDAO
from dao.genres import GenreDAO
from dao.directors import DirectorDAO
from service.movies import MovieService
from service.genres import GenreService
from service.directors import DirectorService

movies_dao = MovieDAO(db.session)
movies_service = MovieService(movies_dao=movies_dao)


genres_dao = GenreDAO(db.session)
genres_service = GenreService(genres_dao=genres_dao)


directors_dao = DirectorDAO(db.session)
directors_service = DirectorService(directors_dao=directors_dao)