from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.equipment import EquipmentModel

class Equipment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('equip_descrip',
                        type=str,
                        required=True,
                        help="Equipment requires descriptions!"
                        )
    parser.add_argument('equip_weight',
                        type=int,
                        required=True,
                        help="Equipment requires weight!"
                        )

    @jwt_required
    def get(self, equip_name):
        equipment = EquipmentModel.find_by_name(equip_name)
        if equipment:
            return equipment.json()
        return {"message": "Equipment not found."}, 404

    @jwt_required
    def post(self, name):
        if EquipmentModel.find_by_name(equip_name):
            return {"message": "Equipment with name '{}' already exists.".format(equip_name)}

        data = Equipment.parser.parse_args()

        equipment = EquipmentModel(equip_name, **data)

        try:
            equipment.save_to_db()
        except:
            return {"message": "An error occurred inserting the equipment."}, 500

        return equipment.json(), 201

    @jwt_required
    def delete(self, name):
        equipment = EquipmentModel.find_by_name(equip_name)

        if equipment:
            equipment.delete_from_db()
            return {"message": "Equipment deleted"}

        return {"message": "Equipment not found"}

    @jwt_required
    def put(self, name):
        data = Equipment.parser.parse_args()

        equipment = EquipmentModel.find_by_name(equip_name)

        if equipment is None:
            equipment = EquipmentModel(equip_name, **data)
        else:
            equipment.descrip = data['equip_descrip']
            equipment.weight = data['equip_weight']

        equipment.save_to_db()

        return equipment.json()

class EquipmentList(Resource):
    @jwt_required
    def get(self):
        return {'equipment': [equipment.json() for equipment in EquipmentModel.query.all()]}
