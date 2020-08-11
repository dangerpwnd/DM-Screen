from marshmallow import Schema, fields, post_load
from models.weapontype import WeaponTypeModel

class WeaponTypeSchema(Schema):
    id_weapontype = fields.Integer(dump_only=True)
    weapontype_name = fields.Str()
    weapon = fields.Nested(WeaponSchema)

    @post_load
    def make_weapontype(self, data, **kwargs):
        return WeaponTypeModel(**data)
