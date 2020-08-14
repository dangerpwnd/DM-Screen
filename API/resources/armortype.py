from flask_restful import Resource, request
from models.armortype import ArmorTypeModel
from schemas.armortype import ArmorTypeSchema

armortype_schema = ArmorTypeSchema()
armortype_list_schema = ArmorTypeSchema(many=True)

class ArmorType(Resource):

    @classmethod
    def get(cls, armortype_name: str):
        armortype = ArmortypeModel.find_by_name(armortype_name)
        if not armortype:
            return {'message': 'Armor type not found.'}, 404
        return armortype_schema.dump(armortype), 200

    @classmethod
    def post(cls, armortype_name: str):
        if ArmortypeModel.find_by_name(armortype_name):
            return {'message': 'Armor type with name "{}" already exists.'.format(armortype_name)}

        armortype_json = request.get_json()
        armortype_json['armortype_name'] = armortype_name

        armortype = armortype_schema.load(armortype_json)
        armortype.save_to_db()
        return armortype_schema.dump(armortype), 201

    @classmethod
    def delete(cls, armortype_name: str):
        armortype = ArmortypeModel.find_by_name(armortype_name)
        if armortype:
            armortype.delete_from_db()
            return {'message': 'Armor type deleted.'}, 200

        return {'message': 'Armor type not found.'}, 404

    # Put method not needed as only single attribute

class ArmorTypeList(Resource):

    @classmethod
    def get(cls):
        return {'Armor Types': armortype_list_schema.dump(ArmorTypeModel.find_all())}
