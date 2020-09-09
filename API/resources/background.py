from flask_restful import Resource, request
from models.background import BackgroundModel
from models.equipment import EquipmentModel
from models.proficiency import ProficiencyModel
from schemas.background import BackgroundSchema

background_schema = BackgroundSchema()
background_list_schema = BackgroundSchema(many=True)


class Background(Resource):
    @classmethod
    def get(cls, background_name: str):
        background = BackgroundModel.find_by_name(background_name)
        if not background:
            return {"message": "Background not found"}, 404
        return background_schema.dump(background), 200

    @classmethod
    def post(cls, background_name: str):
        if BackgroundModel.find_by_name(background_name):
            return (
                {
                    "message": 'A background with name "{}" already exists.'.format(
                        background_name
                    )
                },
                400,
            )

        background_json = request.get_json()
        background_json["background_name"] = background_name

        background = background_schema.load(background_json)

        background.save_to_db()

        return background_schema.dump(background), 201

    @classmethod
    def delete(cls, background_name: str):
        background = BackgroundModel.find_by_name(background_name)

        if background:
            background.delete_from_db()
            return {"message": "Background deleted"}, 200

        return {"message": "Background not found"}, 404

    @classmethod
    def put(cls, background_name: str):
        background_json = request.get_json()
        background = BackgroundModel.find_by_name(background_name)

        if background:
            background.background_descrip = background_json["background_descrip"]
        else:
            background_json["background_name"] = background_name
            background = background_schema.load(background_json)

        background.save_to_db()

        return background_schema.dump(background), 200


class BackgroundList(Resource):
    @classmethod
    def get(cls):
        return (
            {"backgrounds": background_list_schema.dump(BackgroundModel.find_all())},
            200,
        )


class BackgroundHasEquipment(Resource):
    @classmethod
    def post(cls, background_name: str, equip_name: str):
        equipment = EquipmentModel.find_by_name(equip_name)
        background = BackgroundModel.find_by_name(background_name)
        if not equipment:
            return {"message": "Equipment not found."}, 404
        if not background:
            return {"message": "Background not found."}, 404
        background.equipment.append(equipment)
        background.save_to_db()
        return (
            {"message": "Equipment '{}' added.".format(equipment.equip_name)},
            200,
        )


class BackgroundHasProficiencies(Resource):
    @classmethod
    def post(cls, background_name: str, proficiency_name: str):
        proficiency = ProficiencyModel.find_by_name(proficiency_name)
        background = BackgroundModel.find_by_name(background_name)
        if not proficiency:
            return {"message": "Proficiency not found."}, 404
        if not background:
            return {"message": "Background not found."}, 404
        background.proficiencies.append(proficiency)
        background.save_to_db()
        return (
            {"message": "Proficiency '{}' added.".format(proficiency.proficiency_name)},
            200,
        )
