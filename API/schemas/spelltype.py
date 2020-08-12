from marshmallow import Schema, fields, post_load
from models.spelltype import SpellTypeModel

class SpellTypeSchema(Schema):
    id_spelltype = fields.Integer(dump_only=True)
    spelltype_name = fields.Str()
    spell = fields.Nested(SpellSchema)

    @post_load
    def make_spelltype(self, data, **kwargs):
        return SpellTypeModel(**data)
