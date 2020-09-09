from marshmallow import Schema, fields, post_load
from models.subclass import SubClassModel


class SubClassSchema(Schema):
    id_subclass = fields.Integer(dump_only=True)
    subclass_name = fields.Str()
    subclass_descrip = fields.Str()
    class_id = fields.Integer()
    proficiencies = fields.Nested("ProficiencySchema", many=True)
    features = fields.Nested("FeatureSchema", many=True)
    spells = fields.Nested("SpellSchema", many=True)

    @post_load
    def make_charsubclass(self, data, **kwargs):
        return SubClassModel(**data)
