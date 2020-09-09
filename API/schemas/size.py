from marshmallow import Schema, fields, post_load
from models.size import SizeModel


class SizeSchema(Schema):
    id_size = fields.Integer(dump_only=True)
    size_name = fields.Str()

    @post_load
    def make_size(self, data, **kwargs):
        return SizeModel(**data)
