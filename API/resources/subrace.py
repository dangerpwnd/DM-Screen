from flask_restful import Resource, request
from models.subrace import SubRaceModel
from schemas.subrace import SubRaceSchema

subrace_schema = SubRaceSchema()
subrace_list_schema = SubRaceSchema(many=True)


class SubRace(Resource):
    @classmethod
    def get(cls, subrace_name: str):
        subrace = SubraceModel.find_by_name(subrace_name)
        if not subrace:
            return {"message": "Subrace not found"}, 404
        return subrace_schema.dump(subrace), 200

    @classmethod
    def post(cls, subrace_name: str):
        if SubraceModel.find_by_name(subrace_name):
            return (
                {
                    "message": 'A subrace with name "{}" already exists.'.format(
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
        subrace = SubraceModel.find_by_name(subrace_name)

        if subrace:
            subrace.delete_from_db()
            return {"message": "Subrace deleted"}, 200

        return {"message": "Subrace not found"}, 404

    @classmethod
    def put(cls, subrace_name: str):
        subrace_json = request.get_json()
        subrace = subraceModel.find_by_name(subrace_name)

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
        return {"Subraces": subrace_list_schema.dump(SubraceModel.find_all())}, 200


class SubRaceHasFeatures(Resource):
    @classmethod
    def post(cls, subrace_name: str, feature_name: str):
        subrace = SubRaceModel.find_by_name(subrace_name)
        feature = FeatureModel.find_by_name(feature_name)
        if not subrace:
            return {"message": "Subrace not found."}, 404
        if not feature:
            return {"message": "Feature not found."}, 404
        subrace.features.append(feature)
        subrace.save_to_db()
        return (
            {"message": "Feature '{}' added.".format(feature.feature_name)},
            200,
        )


class SubRaceHasProficiencies(Resource):
    @classmethod
    def post(cls, subrace_name: str, proficiency_name: str):
        subrace = SubRaceModel.find_by_name(subrace_name)
        proficiency = ProficiencyModel.find_by_name(proficiency_name)
        if not subrace:
            return {"message": "Subrace not found."}, 404
        if not proficiency:
            return {"message": "Proficiency not found."}, 404
        subrace.proficiencies.append(proficiency)
        subrace.save_to_db()
        return (
            {"message": "Proficiency '{}' added.".format(proficiency.proficiency_name)},
            200,
        )
