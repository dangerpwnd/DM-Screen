from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_claims
from models.equipment import EquipmentModel
from schemas.equipment import EquipmentSchema

equipment_schema = EquipmentSchema()
equipment_list_schema = EquipmentSchema(many=True)

class Equipment(Resource):
    @jwt_required
    @classmethod
    def get(cls, name: str):
        equipment = EquipmentModel.find_by_name(name)
        if not equipment:
            return {"message": "Equipment not found."}, 404
        return equipment_schema.dump(equipment), 200


    @jwt_required
    @classmethod
    def post(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        if EquipmentModel.find_by_name(name):
            return {"message": "Equipment with name '{}' already exists.".format(name)}, 400

        equipment_json = request.get_json()
        equipment = equipment_schema.load(equipment_json)

        try:
            equipment.save_to_db()
        except:
            return {"message": "An error occurred inserting the equipment."}, 500

        return equipment_schema.dump(equipment), 201

    @jwt_required
    @classmethod
    def delete(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        equipment = EquipmentModel.find_by_name(name)

        if equipment:
            equipment.delete_from_db()
            return {"message": "Equipment deleted"}

        return {"message": "Equipment not found"}

    @jwt_required
    @classmethod
    def put(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        equipment_json = request.get_json()
        equipment = EquipmentModel.find_by_name(name)

        if equipment:
            equipment.equip_descrip = equipment_json['equip_descrip']
            equipment.equip_weight = equipment_json['equip_weight']
        else:
            equipment = equipment_schema.load(equipment_json)

        equipment.save_to_db()

        return equipment_schema.dump(equipment), 200

class EquipmentList(Resource):
    @jwt_required
    @classmethod
    def get(cls):
        return {'equipment': equipment_list_schema.dump(EquipmentModel.find_all())}
