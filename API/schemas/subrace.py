from marshmallow import Schema, fields, post_load
from models.subrace import SubRaceModel


class SubRaceSchema(Schema):
    id_subrace = fields.Integer(dump_only=True)
    subrace_name = fields.Str()
    subrace_descrip = fields.Str()
    race_id = fields.Integer()
    race = fields.Nested("RaceSchema")
    features = fields.Nested("FeatureSchema", many=True)
    proficiencies = fields.Nested("ProficiencySchema", many=True)

    @post_load
    def make_subrace(self, data, **kwargs):
        return SubraceModel(**data)
