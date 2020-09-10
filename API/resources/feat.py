from flask_restful import Resource, request
from models.feat import FeatModel
from schemas.feat import FeatSchema

feat_schema = FeatSchema()
feat_list_schema = FeatSchema(many=True)


class Feat(Resource):
    @classmethod
    def get(cls, feat_name: str):
        feat = FeatModel.find_by_name(feat_name)
        if not feat:
            return {"message": "Feat not found."}, 404
        return feat_schema.dump(feat), 200

    @classmethod
    def post(cls, feat_name: str):
        if FeatModel.find_by_name(feat_name):
            return {"message": 'Feat with name "{}" already exists.'.format(feat_name)}

        feat_json = request.get_json()
        feat_json["feat_name"] = feat_name

        feat = feat_schema.load(feat_json)
        feat.save_to_db()
        return feat_schema.dump(feat), 201

    @classmethod
    def delete(cls, feat_name: str):
        feat = FeatModel.find_by_name(feat_name)
        if feat:
            feat.delete_from_db()
            return {"message": "Feat deleted."}, 200

        return {"message": "Feat not found."}, 404

    @classmethod
    def put(cls, feat_name: str):
        feat_json = request.get_json()
        feat = FeatModel.find_by_name(feat_name)

        if feat:
            feat.feat_descrip = feat_json["feat_descrip"]
        else:
            feat_json["feat_name"] = feat_name
            feat = feat_schema.load(feat_json)

        feat.save_to_db()

        return feat_schema.dump(feat), 200


class FeatList(Resource):
    @classmethod
    def get(cls):
        return {"Feats": feat_list_schema.dump(FeatModel.find_all())}

class FeatHasProficiencies(Resource):
    @classmethod
    def post(cls, feat_name: str, proficiency_name: str):
        feat = FeatModel.find_by_name(feat_name)
        proficiency = ProficiencyModel.find_by_name(proficiency_name)
        if not feat:
            return {"message": "Feat not found."}, 404
        if not proficiency:
            return {"message": "Proficiency not found."}, 404
        feat.proficiencies.append(proficiency)
        feat.save_to_db()
        return (
            {"message": "Proficiency '{}' added.".format(proficiency.equip_name)},
            200,
        )
