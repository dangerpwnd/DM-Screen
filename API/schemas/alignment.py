from marshmallow import Schema, fields, post_load
from models.alignment import AlignmentModel

class AlignmentSchema(Schema):
    id_alignment = fields.Integer(dump_only=True)
    alignment_name = fields.Str()
    alignment_descrip = fields.Str()


    @post_load
    def make_alignment(self, data, **kwargs):
        return AlignmentModel(**data)
