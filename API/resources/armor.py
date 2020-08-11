from flask_restful import Resource, request
from models.armor import ArmorModel
from schemas.armor import ArmorSchema

armor_schema = ArmorSchema()
armor_list_schema = ArmorSchema(many=True)

class Armor(Resource):

    @classmethod
    def get(cls, armor_name: str):
        armor = ArmorModel.find_by_name(armor_name)
        if not armor:
            return {'message': 'Armor not found.'}, 404
        return armor_schema.dump(armor), 200

    @classmethod
    def post(cls, armor_name: str):
        if ArmorModel.find_by_name(armor_name):
            return {'message': 'Armor with name "{}" already exists.'.format(armor_name)}

        armor_json = request.get_json()
        armor_json['armor_name'] = armor_name

        armor = armor_schema.load(armor_json)
        armor.save_to_db()
        return armor_schema.dump(skill), 201

    @classmethod
    def delete(cls, armor_name: str):
        armor = ArmorModel.find_by_name(armor_name)
        if armor:
            armor.delete_from_db()
            return {'message': 'Armor deleted.'}, 200

        return {'message': 'Armor not found.'}, 404

    @classmethod
    def put(cls, armor_name: str):
        armor_json = request.get_json()
        skill = ArmorModel.find_by_name(armor_name)

        if armor:
            armor.armor_descrip = armor_json['armor_descrip']
            armor.armor_ac = armor_json['armor_ac']
            armor.armor_weight = armor_json['armor_weight']
            armor.armor_maxdex = armor_json['armor_maxdex']
        else:
            armor_json['armor_name'] = armor_name
            armor = armor_schema.load(armor_json)

        armor.save_to_db()

        return armor_schema.dump(armor), 200

class ArmorList(Resource):

    @classmethod
    def get(cls):
        return {'Armor': Armor_list_schema.dump(ArmorModel.find_all())}
