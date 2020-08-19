from marshmallow import Schema, fields, post_load
from models.armortype import ArmorTypeModel

class ArmorTypeSchema(Schema):
    id_armortype = fields.Integer(dump_only=True)
    armortype_name = fields.Str()
    armor = fields.Nested('ArmorSchema')

    @post_load
    def make_armortype(self, data, **kwargs):
        return ArmorTypeModel(**data)

class ArmorSchema(Schema):
    id_armor = fields.Integer()
    armor_name = fields.Str()
    armor_descrip = fields.Str()
    armor_ac = fields.Integer()
    armor_weight = fields.Integer()
    armor_maxdex = fields.Integer()
