from marshmallow import Schema, fields, post_load
from models.armor import ArmorModel

class ArmorSchema(Schema):
    id_armor = fields.Integer(dump_only=True)
    armor_name = fields.Str()
    armor_descrip = fields.Str()
    armor_ac = fields.Integer()
    armor_weight = fields.Integer()
    armor_maxdex = fields.Integer()
    armor_type = fields.Nested(ArmorTypeSchema)

    @post_load
    def make_armor(self, data, **kwargs):
        return ArmorModel(**data)
