from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_claims
from marshmallow import ValidationError
from models.background import BackgroundModel
from schemas.background import BackgroundSchema

background_schema = BackgroundSchema()
background_list_schema = BackgroundSchema(many=True)

class Background(Resource):
    @jwt_required
    @classmethod
    def get(cls, name: str):
        background = BackgroundModel.find_by_name(name)
        if not background:
            return {'message': 'Background not found'}, 404
        return background_schema.dump(background), 200

    @jwt_required
    @classmethod
    def post(cls, name: str):
        if BackgroundModel.find_by_name(name):
            return {'message': 'A background with name "{}" already exists.'.format(name)}, 400

        background_json = request.get_json()
        background

        try:
            background.save_to_db()
        except:
            return {"message": "An error occurred inserting the background."}, 500

        return background.json(), 201

    @jwt_required
    def delete(self, background_name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

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
