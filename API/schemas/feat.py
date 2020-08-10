from marshmallow import Schema, fields, post_load
from models.feat import FeatModel

class FeatSchema(Schema):
    id_feat = fields.Integer(dump_only=True)
    feat_name = fields.Str()
    feat_descrip = fields.Str()

    @post_load
    def make_feat(self, data, **kwargs):
        return FeatModel(**data)
