from flask_restful import Resource, request
from models.proficiency import ProficiencyModel
from schemas.proficiency import ProficiencySchema

proficiency_schema = ProficiencySchema()
proficiency_list_schema = ProficiencySchema(many=True)


class Proficiency(Resource):
    @classmethod
    def get(cls, proficiency_name: str):
        proficiency = ProficiencyModel.find_by_name(proficiency_name)
        if not proficiency:
            return {"message": "Proficiency not found."}, 404
        return proficiency_schema.dump(proficiency), 200

    @classmethod
    def post(cls, proficiency_name: str):

        if ProficiencyModel.find_by_name(proficiency_name):
            return {
                "message": "Proficiency with name '{}' already exists.".format(
                    proficiency_name
                )
            }

        proficiency_json = request.get_json()
        proficiency_json["proficiency_name"] = proficiency_name

        proficiency = proficiency_schema.load(proficiency_json)

        proficiency.save_to_db()

        return proficiency_schema.dump(proficiency), 201

    @classmethod
    def delete(cls, proficiency_name: str):

        proficiency = ProficiencyModel.find_by_name(proficiency_name)

        if proficiency:
            proficiency.delete_from_db()
            return {"message": "Proficiency deleted"}

        return {"message": "Proficiency not found"}

    @classmethod
    def put(cls, proficiency_name: str):

        proficiency_json = request.get_json()
        proficiency = ProficiencyModel.find_by_name(proficiency_name)

        if proficiency:
            proficiency.proficiency_descrip = proficiency_json["proficiency_descrip"]
        else:
            proficiency_json["proficiency_name"] = proficiency_name
            proficiency = proficiency_schema.load(proficiency_json)

        proficiency.save_to_db()

        return proficiency_schema.dump(proficiency), 200


class ProficiencyList(Resource):
    @classmethod
    def get(cls):
        return {
            "Proficiencies": proficiency_list_schema.dump(ProficiencyModel.find_all())
        }
