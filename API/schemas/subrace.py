from marshmallow import Schema, fields, post_load
from models.subrace import SubraceModel

class SubraceSchema(Schema):
    id_subrace = fields.Integer(dump_only=True)
    subrace_name = fields.Str()
    subrace_descrip = fields.Str()
    race_id = fields.Integer()
    features = fields.Nested('FeatureSchema', many=True)
    proficiencies = fields.Nested('ProficiencySchema', many=True)

    @post_load
    def make_subrace(self, data, **kwargs):
        return SubraceModel(**data)
