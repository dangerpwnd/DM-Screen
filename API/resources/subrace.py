from flask_restful import Resource, request
from models.subrace import SubRaceModel
from models.feature import FeatureModel
from models.proficiency import ProficiencyModel
from schemas.subrace import SubRaceSchema

subrace_schema = SubRaceSchema()
subrace_list_schema = SubRaceSchema(many=True)


class SubRace(Resource):
    @classmethod
    def get(cls, subrace_name: str):
        subrace = SubRaceModel.find_by_name(subrace_name)
        if not subrace:
            return {"message": "Sub race not found"}, 404
        return subrace_schema.dump(subrace), 200

    @classmethod
    def post(cls, subrace_name: str):
        if SubRaceModel.find_by_name(subrace_name):
            return (
                {
                    "message": 'A sub race with name "{}" already exists.'.format(
                        subrace_name
                    )
                },
                400,
            )

        subrace_json = request.get_json()
        subrace_json["subrace_name"] = subrace_name

        subrace = subrace_schema.load(subrace_json)

        subrace.save_to_db()

        return subrace_schema.dump(subrace), 201

    @classmethod
    def delete(cls, subrace_name: str):
        subrace = SubRaceModel.find_by_name(subrace_name)

        if subrace:
            subrace.delete_from_db()
            return {"message": "Sub race deleted"}, 200

        return {"message": "Sub race not found"}, 404

    @classmethod
    def put(cls, subrace_name: str):
        subrace_json = request.get_json()
        subrace = SubRaceModel.find_by_name(subrace_name)

        if subrace:
            subrace.subrace_descrip = subrace_json["subrace_descrip"]
            subrace.race_id = subrace_json["race_id"]
        else:
            subrace_json["subrace_name"] = subrace_name
            subrace = subrace_schema.load(subrace_json)

        subrace.save_to_db()

        return subrace_schema.dump(subrace), 200


class SubRaceList(Resource):
    @classmethod
    def get(cls):
        return {"Subraces": subrace_list_schema.dump(SubRaceModel.find_all())}, 200


class SubRaceHasTraits(Resource):
    @classmethod
    def post(cls, subrace_name: str, trait_name: str):
        subrace = SubRaceModel.find_by_name(subrace_name)
        trait = TraitModel.find_by_name(trait_name)
        if not subrace:
            return {"message": "Sub race not found."}, 404
        if not trait:
            return {"message": "Trait not found."}, 404
        subrace.proficiencies.append(trait)
        subrace.save_to_db()
        return (
            {"message": "Trait '{}' added.".format(trait.trait_name)},
            200,
        )
