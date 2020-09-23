from marshmallow import Schema, fields, post_load
from models.race import RaceModel


class RaceSchema(Schema):
    id_race = fields.Integer(dump_only=True)
    race_name = fields.Str()
    race_descrip = fields.Str()
    race_min_age = fields.Integer()
    race_max_age = fields.Integer()
    race_min_height = fields.Integer()
    race_max_height = fields.Integer()
    race_speed = fields.Integer()
    size_id = fields.Integer()
    size = fields.Nested("SizeSchema")
    traits = fields.Nested("TraitSchema", many=True)
    languages = fields.Nested("LanguageSchema", many=True)
    subraces = fields.Nested("SubRaceSchema", many=True)

    @post_load
    def make_race(self, data, **kwargs):
        return RaceModel(**data)
