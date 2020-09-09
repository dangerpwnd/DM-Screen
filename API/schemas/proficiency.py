from marshmallow import Schema, fields, post_load
from models.proficiency import ProficiencyModel


class ProficiencySchema(Schema):
    id_proficiency = fields.Integer(dump_only=True)
    proficiency_name = fields.Str()
    proficiency_descrip = fields.Str()

    @post_load
    def make_proficiency(self, data, **kwargs):
        return ProficiencyModel(**data)
