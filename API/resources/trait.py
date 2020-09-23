from flask_restful import Resource, request
from models.trait import TraitModel
from schemas.trait import TraitSchema

trait_schema = TraitSchema()
trait_list_schema = TraitSchema(many=True)


class Trait(Resource):
    @classmethod
    def get(cls, trait_name: str):
        trait = TraitModel.find_by_name(trait_name)
        if not trait:
            return {"message": "Trait not found."}, 404
        return trait_schema.dump(trait), 200

    @classmethod
    def post(cls, trait_name: str):

        if TraitModel.find_by_name(trait_name):
            return {
                "message": "Proficiency with name '{}' already exists.".format(
                    trait_name
                )
            }

        trait_json = request.get_json()
        trait_json["trait_name"] = trait_name

        trait = trait_schema.load(trait_json)

        trait.save_to_db()

        return trait_schema.dump(trait), 201

    @classmethod
    def delete(cls, trait_name: str):

        trait = TraitModel.find_by_name(trait_name)

        if trait:
            trait.delete_from_db()
            return {"message": "Trait deleted"}

        return {"message": "Trait not found"}

    @classmethod
    def put(cls, trait_name: str):

        trait_json = request.get_json()
        trait = TraitModel.find_by_name(trait_name)

        if trait:
            trait.trait_descrip = trait_json["trait_descrip"]
        else:
            trait_json["trait_name"] = trait_name
            trait = trait_schema.load(trait_json)

        trait.save_to_db()

        return trait_schema.dump(trait), 200


class ProficiencyList(Resource):
    @classmethod
    def get(cls):
        return {
            "Proficiencies": trait_list_schema.dump(TraitModel.find_all())
        }
