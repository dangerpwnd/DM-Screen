from marshmallow import Schema, fields, post_load
from models.skin import SkinModel

class SkinSchema(Schema):
    id_skin = fields.Integer(dump_only=True)
    skin_color = fields.Str()

    @post_load
    def make_skin(self, data, **kwargs):
        return SkinModel(**data)
