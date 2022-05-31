from dao.model.directors import Director, DirectorSchema


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = Director.query.all()
        result = DirectorSchema(many=True).dump(directors)
        return result


    def get_one(self, id):
        directors = Director.query.get(id)
        return directors