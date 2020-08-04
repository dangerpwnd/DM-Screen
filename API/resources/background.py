from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_claims
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
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        if BackgroundModel.find_by_name(name):
            return {'message': 'A background with name "{}" already exists.'.format(name)}, 400

        background_json = request.get_json()
        background_json['background_name'] = name
        background = background_schema.load(background_json)

        try:
            background.save_to_db()
        except:
            return {"message": "An error occurred inserting the background."}, 500

        return background_schema.dump(background), 201

    @jwt_required
    @classmethod
    def delete(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        background = BackgroundModel.find_by_name(name)

        if background:
            background.delete_from_db()
            return {"message": "Background deleted"}

        return {"message": "Background not found"}

    @jwt_required
    @classmethod
    def put(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        background_json = request.get_json()
        background = BackgroundModel.find_by_name(name)

        if background:
            background.background_descrip = background_json['background_descrip']
        else:
            background_json['background_name'] = name
            background = background_schema.load(background_json)

        background.save_to_db()

        return background_schema.dump(background), 200

class BackgroundList(Resource):
    @jwt_required
    @classmethod
    def get(cls):
        return {'backgrounds': background_list_schema.dump(BackgroundModel.find_all())}
