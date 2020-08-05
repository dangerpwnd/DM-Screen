from flask_restful import Resource, request
from models.equipment import EquipmentModel
from schemas.equipment import EquipmentSchema

equipment_schema = EquipmentSchema()
equipment_list_schema = EquipmentSchema(many=True)

class Equipment(Resource):

    @classmethod
    def get(cls, equip_name: str):
        equipment = EquipmentModel.find_by_name(equip_name)
        if not equipment:
            return {"message": "Equipment not found."}, 404
        return equipment_schema.dump(equipment), 200


    @classmethod
    def post(cls, equip_name: str):

        if EquipmentModel.find_by_name(equip_name):
            return {"message": "Equipment with name '{}' already exists.".format(equip_name)}, 400

        equipment_json = request.get_json()
        equipment_json["equip_name"] = equip_name

        equipment = equipment_schema.load(equipment_json)

        equipment.save_to_db()

        return equipment_schema.dump(equipment), 201

    @classmethod
    def delete(cls, equip_name: str):

        equipment = EquipmentModel.find_by_name(equip_name)

        if equipment:
            equipment.delete_from_db()
            return {"message": "Equipment deleted"}

        return {"message": "Equipment not found"}

    @classmethod
    def put(cls, equip_name: str):

        equipment_json = request.get_json()
        equipment = EquipmentModel.find_by_name(equip_name)

        if equipment:
            equipment.equip_descrip = equipment_json['equip_descrip']
            equipment.equip_weight = equipment_json['equip_weight']
        else:
            equipment_json['equip_name'] = equip_name
            equipment = equipment_schema.load(equipment_json)

        equipment.save_to_db()

        return equipment_schema.dump(equipment), 200

class EquipmentList(Resource):

    @classmethod
    def get(cls):
        return {'equipment': equipment_list_schema.dump(EquipmentModel.find_all())}
