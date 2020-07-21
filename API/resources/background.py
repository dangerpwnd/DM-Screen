from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.background import BackgroundModel
from app import BackgroundSchema


# Variables
background_schema = BackgroundSchema()
backgrounds_schema = BackgroundSchema(many=True)

class Background(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('background_descrip',
                         type=str,
                         required=True,
                         help="Background requires descriptions!"
                         )
    @jwt_required
    def get(self, background_name):
        background = BackgroundModel.find_by_name(background_name)
        if background:
            return background.json()
        return {'message': 'Background not found'}, 404

    @jwt_required
    def post(self, back_name):
        if BackgroundModel.find_by_name(background_name):
            return {'message': 'A background with name "{}" already exists.'.format(background_name)}

        data = Background.parser.parse_args()

        background = BackgroundModel(background_name, **data)

        try:
            background.save_to_db()
        except:
            return {"message": "An error occurred inserting the background."}, 500

        return background.json(), 201

    @jwt_required
    def delete(self, background_name):
        background = BackgroundModel.find_by_name(background_name)

        if background:
            background.delete_from_db()
            return {"message": "Background deleted"}

        return {"message": "Background not found"}

    @jwt_required
    def put(self, background_name):
        data = Background.parser.parse_args()

        background = BackgroundModel.find_by_name(background_name)

        if background is None:
            background = BackgroundModel(background_name, **data)
        else:
            background.descrip = data['background_descrip']

        background.save_to_db()

        return background.json()

class BackgroundList(Resource):
    @jwt_required
    def get(self):
        return {'backgrounds': [background.json() for background in BackgroundModel.find_all()]}
