from marshmallow import Schema, fields, post_load
from models.charattribute import CharAttributeModel


class CharAttributeSchema(Schema):
    id_attribute = fields.Integer(dump_only=True)
    attribute_name = fields.Str()
    attribute_descrip = fields.Str()

    @post_load
    def make_attribute(self, data, **kwargs):
        return CharAttributeModel(**data)
