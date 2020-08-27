from flask_restful import Resource, request
from models.background import BackgroundModel, EquipAssocModel, ProficiencyAssocModel
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
    def get(cls, id_background: int, id_equip: int):
        background = BackgroundModel.find_by_id(id_background)
        equipment = EquipmentModel.find_by_id(id_equip)
        if not background:
            return {"message": "Background not found."}, 404
        if not equipment:
            return {"message": "Equipment not found."}, 404

        return (
            {
                "message": "Background '{}' and Equipment '{}' found.".format(
                    background.background_name, equipment.equip_name
                )
            },
            200,
        )

    @classmethod
    def post(cls, id_background: int, id_equip: int):
        background = BackgroundModel.find_by_id(id_background)
        equipment = EquipmentModel.find_by_id(id_equip)
        if not background:
            return {"message": "Background not found."}, 404
        if not equipment:
            return {"message": "Equipment not found."}, 404

        background_equipment = EquipAssocModel()
        background_equipment.background_id = id_background
        background_equipment.equip_id = id_equip
        background_equipment.save_to_db()
        return (
            {
                "message": "Equipment '{}' added to background '{}'.".format(
                    equipment.equip_name, background.background_name
                )
            },
            200,
        )


class BackgroundHasProficiencies(Resource):
    @classmethod
    def get(cls, id_background: int, id_proficiency: int):
        background = BackgroundModel.find_by_id(id_background)
        proficiency = ProficiencyModel.find_by_id(id_proficiency)
        if not background:
            return {"message": "Background not found."}, 404
        if not proficiency:
            return {"message": "Proficiency not found."}, 404

        return (
            {
                "message": "Background '{}' and Proficiency '{}' found.".format(
                    background.background_name, proficiency.proficiency_name
                )
            },
            200,
        )

    @classmethod
    def post(cls, id_background: int, id_proficiency: int):
        background = BackgroundModel.find_by_id(id_background)
        proficiency = ProficiencyModel.find_by_id(id_proficiency)
        if not background:
            return {"message": "Background not found."}, 404
        if not proficiency:
            return {"message": "Proficiency not found."}, 404

        background_proficiency = ProficiencyAssocModel(id_background, id_proficiency)
        background_proficiency.save_to_db()
        return (
            {
                "message": "Proficiency '{}' added to background '{}' and  found.".format(
                    proficiency.proficiency_name, background.background_name
                )
            },
            200,
        )
