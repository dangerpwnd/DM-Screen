from marshmallow import Schema, fields, post_load
from models.hair import HairModel

class HairSchema(Schema):
    id_hair = fields.Integer(dump_only=True)
    hair_color = fields.Str()

    @post_load
    def make_hair(self, data, **kwargs):
        return HairModel(**data)
