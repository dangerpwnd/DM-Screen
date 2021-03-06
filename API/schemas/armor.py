from marshmallow import Schema, fields, post_load
from models.armor import ArmorModel


class ArmorSchema(Schema):
    id_armor = fields.Integer(dump_only=True)
    armor_name = fields.Str()
    armor_descrip = fields.Str()
    armor_ac = fields.Integer()
    armor_weight = fields.Integer()
    armor_cost = fields.Str()
    armor_minstr = fields.Integer()
    armor_maxdex = fields.Integer()
    armortype_id = fields.Integer()
    armortype = fields.Nested("ArmorTypeSchema")

    @post_load
    def make_armor(self, data, **kwargs):
        return ArmorModel(**data)
