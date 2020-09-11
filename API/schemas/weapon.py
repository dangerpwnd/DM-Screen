from marshmallow import Schema, fields, post_load
from models.weapon import WeaponModel


class WeaponSchema(Schema):
    id_weapon = fields.Integer(dump_only=True)
    weapon_name = fields.Str()
    weapon_descrip = fields.Str()
    weapon_damage = fields.Str()
    weapon_weight = fields.Integer()
    weapontype_id = fields.Integer()
    weapontype = fields.Nested("WeaponTypeSchema")

    @post_load
    def make_weapon(self, data, **kwargs):
        return WeaponModel(**data)
