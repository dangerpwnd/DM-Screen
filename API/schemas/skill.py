from marshmallow import Schema, fields, post_load
from models.skill import SkillModel

class SkillSchema(Schema):
    id_skill = fields.Integer(dump_only=True)
    skill_name = fields.Str()
    skill_descrip = fields.Str()

    @post_load
    def make_skill(self, data, **kwargs):
        return SkillModel(**data)
