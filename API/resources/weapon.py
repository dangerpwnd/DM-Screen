from flask_restful import Resource, request
from models.weapon import WeaponModel
from schemas.weapon import WeaponSchema

weapon_schema = WeaponSchema()
weapon_list_schema = WeaponSchema(many=True)


class Weapon(Resource):
    @classmethod
    def get(cls, weapon_name: str):
        weapon = WeaponModel.find_by_name(weapon_name)
        if not weapon:
            return {"message": "Weapon not found."}, 404
        return weapon_schema.dump(weapon), 200

    @classmethod
    def post(cls, weapon_name: str):
        if WeaponModel.find_by_name(weapon_name):
            return {
                "message": 'Weapon with name "{}" already exists.'.format(weapon_name)
            }

        weapon_json = request.get_json()
        weapon_json["weapon_name"] = weapon_name

        weapon = weapon_schema.load(weapon_json)
        weapon.save_to_db()
        return weapon_schema.dump(weapon), 201

    @classmethod
    def delete(cls, weapon_name: str):
        weapon = WeaponModel.find_by_name(weapon_name)
        if weapon:
            weapon.delete_from_db()
            return {"message": "Weapon deleted."}, 200

        return {"message": "Weapon not found."}, 404

    @classmethod
    def put(cls, weapon_name: str):
        weapon_json = request.get_json()
        weapon = WeaponModel.find_by_name(weapon_name)

        if weapon:
            weapon.weapon_descrip = weapon_json["weapon_descrip"]
            weapon.weapon_damage = weapon_json["weapon_damage"]
            weapon.weapon_weight = weapon_json["weapon_weight"]
            weapon.weapontype_id = weapon_json["weapontype_id"]
        else:
            weapon_json["weapon_name"] = weapon_name
            weapon = weapon_schema.load(weapon_json)

        weapon.save_to_db()

        return weapon_schema.dump(weapon), 200


class WeaponList(Resource):
    @classmethod
    def get(cls):
        return {"Weapons": weapon_list_schema.dump(WeaponModel.find_all())}
