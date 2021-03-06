from marshmallow import Schema, fields, post_load
from models.subrace import SubRaceModel


class SubRaceSchema(Schema):
    id_subrace = fields.Integer(dump_only=True)
    subrace_name = fields.Str()
    subrace_descrip = fields.Str()
    race = fields.Nested("RaceSchema")
    traits = fields.Nested("TraitSchema", many=True)

    @post_load
    def make_subrace(self, data, **kwargs):
        return SubRaceModel(**data)
