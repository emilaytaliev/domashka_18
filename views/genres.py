from flask_restx import Resource, Namespace
from implemented import genres_service
from dao.model.genres import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        genre = genres_service.get_all()
        result = GenreSchema(many=True).dump(genre)
        return result, 200


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genres_service.get_one(id)
        result = GenreSchema().dump(genre)
        return result, 200
