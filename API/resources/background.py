from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.background import BackgroundModel

class Background(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('back_descrip',
                         type=str,
                         required=True,
                         help="Background requires descriptions!"
                         )
    @jwt_required
    def get(self, back_name):
        background = BackgroundModel.find_by_name(back_name)
        if background:
            return background.json()
        return {'message': 'Background not found'}, 404

    @jwt_required
    def post(self, back_name):
        if BackgroundModel.find_by_name(back_name):
            return {'message': 'A background with name "{}" already exists.'.format(back_name)}

        data = Background.parser.parse_args()

        background = BackgroundModel(back_name, **data)

        try:
            background.save_to_db()
        except:
            return {"message": "An error occurred inserting the background."}, 500

        return background.json(), 201

    @jwt_required
    def delete(self, back_name):
        background = BackgroundModel.find_by_name(back_name)

        if background:
            background.delete_from_db()
            return {"message": "Background deleted"}

        return {"message": "Background not found"}

    @jwt_required
    def put(self, back_name):
        data = Background.parser.parse_args()

        background = BackgroundModel.find_by_name(back_name)

        if background is None:
            background = BackgroundModel(back_name, **data)
        else:
            background.descrip = data['back_descrip']

        background.save_to_db()

        return background.json()

class BackgroundList(Resource):
    @jwt_required
    def get(self):
        return {"backgrounds": [background.json() for background in BackgroundModel.query.all()]}
