from flask_restx import Resource, Namespace
from implemented import movies_service
from flask import request
from dao.model.movies import MovieSchema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        years = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if years:
            movies = movies_service.get_be_years(years)
        elif director_id:
            movies = movies_service.get_be_directors(director_id)

        elif genre_id:
            movies = movies_service.get_be_genre(genre_id)



        else:
            movies = movies_service.get_all()
        result = MovieSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        data = request.get_json()
        movies_service.create(data)
        return "", 201



@movies_ns.route('/<int:id>')
class MoviesView(Resource):
    def get(self, id):
        movies = movies_service.get_one(id)
        result = MovieSchema().dump(movies)
        return result, 200

    def put(self, id):
        data = request.get_json()
        movies_service.update(data)

        return "", 204

    def delete(self, id):
        data = request.get_json()
        movies_service.delete(id)
        return "", 204



