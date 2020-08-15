from marshmallow import Schema, fields, post_load
from models.charclass import CharClassModel

class CharClassSchema(Schema):
    id_class = fields.Integer(dump_only=True)
    class_name = fields.Str()
    class_descrip = fields.Str()
    equipment = fields.Nested('EquipmentSchema', many=True)
    proficiencies = fields.Nested('ProficiencySchema', many=True)
    features = fields.Nested('FeatureSchema', many=True)
    skills = fields.Nested('SkillSchema', many=True)
    spells = fields.Nested('SpellSchema', many=True)
    languages = fields.Nested('LanguageSchema', many=True)

    @post_load
    def make_charclass(self, data, **kwargs):
        return CharClassModel(**data)
