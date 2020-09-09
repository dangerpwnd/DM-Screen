from marshmallow import Schema, fields, post_load
from models.eye import EyeModel


class EyeSchema(Schema):
    id_eye = fields.Integer(dump_only=True)
    eye_color = fields.Str()

    @post_load
    def make_eye(self, data, **kwargs):
        return EyeModel(**data)
