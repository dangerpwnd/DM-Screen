from marshmallow import Schema, fields, post_load
from models.spell import SpellModel


class SpellSchema(Schema):
    id_spell = fields.Integer(dump_only=True)
    spell_name = fields.Str()
    spell_descrip = fields.Str()
    spell_amount = fields.Str()
    is_racial = fields.Boolean()
    spell_type = fields.Nested("SpellTypeSchema")

    @post_load
    def make_spell(self, data, **kwargs):
        return SpellModel(**data)
