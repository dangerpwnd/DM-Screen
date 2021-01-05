from marshmallow import Schema, fields, post_load
from models.feature import FeatureModel


class FeatureSchema(Schema):
    id_feature = fields.Integer(dump_only=True)
    feature_name = fields.Str()
    feature_descrip = fields.Str()
    feature_customvalue = fields.Str()

    @post_load
    def make_feature(self, data, **kwargs):
        return FeatureModel(**data)
