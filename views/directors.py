from flask_restx import Resource, Namespace
from implemented import directors_service
from dao.model.directors import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        director = directors_service.get_all()
        result = DirectorSchema(many=True).dump(director)
        return result, 200


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = directors_service.get_one(id)
        result = DirectorSchema().dump(director)
        return result, 200