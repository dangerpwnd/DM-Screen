from marshmallow import Schema, fields, post_load
from models.faction import FactionModel

class FactionSchema(Schema):
    id_faction = fields.Integer(dump_only=True)
    faction_name = fields.Str()
    faction_descrip = fields.Str()

    @post_load
    def make_faction(self, data, **kwargs):
        return FactionModel(**data)
