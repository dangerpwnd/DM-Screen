from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.background import BackgroundModel

class Background(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('descrip',
                         type=str,
                         required=True,
                         help="Background requires descriptions!"
                         )
    @jwt_required
    def get(self, name):
        background = BackgroundModel.find_by_name(name)

        if background:
            return background.json()
        return {"message": "Background not found"}, 404

    @jwt_required
    def post(self, name):
        if BackgroundModel.find_by_name(name):
            return {"message": "A background with name '{}' already exists.".format(name)}

        data = Background.parser.parse_args()

        background = BackgroundModel(name, **data)

        try:
            background.save_to_db()
        except:
            return {"message": "An error occurred inserting the background."}, 500

        return background.json(), 201

    @jwt_required
    def delete(self, name):
        background = BackgroundModel.find_by_name(name)

        if background:
            background.delete_from_db()
            return {"message": "Background deleted"}

        return {"message": "Background not found"}

    @jwt_required
    def put(self, name):
        data = Background.parser.parse_args()

        background = BackgroundModel.find_by_name(name)

        if background is None:
            background = BackgroundModel(name, **data)
        else:
            background.descrip = data['descrip']

        background.save_to_db()

        return background.json()

class BackgroundList(Resource):
    @jwt_required
    def get(self):
        return {'Backgrounds': [background.json() for background in BackgroundModel.query.all()]}
