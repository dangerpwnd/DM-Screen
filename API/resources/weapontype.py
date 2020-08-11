from flask_restful import Resource, request
from models.weapon import WeaponTypeModel
from schemas.weapon import WeaponTypeSchema

weapontype_schema = WeaponTypeSchema()
weapontype_list_schema = WeaponTypeSchema(many=True)

class WeaponType(Resource):

    @classmethod
    def get(cls, weapontype_name: str):
        weapontype = WeaponTypeModel.find_by_name(weapontype_name)
        if not weapontype:
            return {'message': 'Weapon type not found.'}, 404
        return weapontype_schema.dump(weapontype), 200

    @classmethod
    def post(cls, weapontype_name: str):
        if WeaponTypeModel.find_by_name(weapontype_name):
            return {'message': 'Weapon type with name "{}" already exists.'.format(weapontype_name)}

        weapontype_json = request.get_json()
        weapontype_json['weapontype_name'] = weapontype_name

        weapontype = weapontype_schema.load(weapontype_json)
        weapontype.save_to_db()
        return weapontype_schema.dump(skill), 201

    @classmethod
    def delete(cls, weapontype_name: str):
        weapontype = WeaponTypeModel.find_by_name(weapontype_name)
        if weapontype:
            weapontype.delete_from_db()
            return {'message': 'Weapon type deleted.'}, 200

        return {'message': 'Weapon type not found.'}, 404

    # Put method not needed as only single attribute

class WeaponTypeList(Resource):

    @classmethod
    def get(cls):
        return {'Weapon Types': weapontype_list_schema.dump(WeaponTypeModel.find_all())}
