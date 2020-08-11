from marshmallow import Schema, fields, post_load
from models.armortype import ArmorTypeModel

class ArmorTypeSchema(Schema):
    id_armortype = fields.Integer(dump_only=True)
    armortype_name = fields.Str()
    armor = fields.Nested(ArmorSchema)

    @post_load
    def make_armortype(self, data, **kwargs):
        return ArmorTypeModel(**data)
