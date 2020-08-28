from marshmallow import Schema, fields, post_load
from models.background import BackgroundModel

class BackgroundSchema(Schema):
    id_background = fields.Integer(dump_only=True)
    background_name = fields.Str()
    background_descrip = fields.Str()
    equipment = fields.List(fields.Nested('EquipmentSchema', many=True))
    proficiencies = fields.Nested('ProficiencySchema', many=True)

    @post_load
    def make_background(self, data, **kwargs):
        return BackgroundModel(**data)
