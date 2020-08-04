from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims
from models.proficiency import ProficiencyModel
from schemas.proficiency import ProficiencySchema

proficiency_schema = ProficiencySchema()
proficiency_list_schema = ProficiencySchema(many=True)

class Proficiency(Resource):
    @jwt_required
    @classmethod
    def get(cls, name: str):
        proficiency = ProficiencyModel.find_by_name(name)
        if not proficiency:
            return {"message": "Proficiency not found."}, 404
        return proficiency_schema.dump(proficiency), 200

    @jwt_required
    @classmethod
    def post(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        if ProficiencyModel.find_by_name(name):
            return {"message": "Proficiency with name '{}' already exists.".format(name)}

        proficiency_json = request.get_json()
        proficiency_json['proficiency_name'] = name
        proficiency = proficiency_schema.load(proficiency)

        try:
            proficiency.save_to_db()
        except:
            return {"message": "An error occurred inserting the proficiency."}, 500

        return proficiency_schema.dump(proficiency), 201

    @jwt_required
    @classmethod
    def delete(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        proficiency = ProficiencyModel.find_by_name(name)

        if proficiency:
            proficiency.delete_from_db()
            return {"message": "Proficiency deleted"}

        return {"message": "Proficiency not found"}

    @jwt_required
    @classmethod
    def put(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        proficiency_json = request.get_json()
        proficiency = ProficiencyModel.find_by_name(name)

        if proficiency:
            proficiency.proficiency_descrip = proficiency_json['proficiency_descrip']
        else:
            proficiency_json['proficiency_name'] = name
            proficiency = proficiency_schema.load(proficiency_json)

        proficiency.save_to_db()

        return proficiency_schema.dump(proficiency), 200

class ProficiencyList(Resource):
    @jwt_required
    @classmethod
    def get(cls):
        return {'Proficiency': proficiency_list_schema.dump(ProficiencyModel.find_all())}
