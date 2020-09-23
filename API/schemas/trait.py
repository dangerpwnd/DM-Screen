from marshmallow import Schema, fields, post_load
from models.trait import TraitModel


class TraitSchema(Schema):
    id_trait = fields.Integer(dump_only=True)
    trait_name = fields.Str()
    trait_descrip = fields.Str()

    @post_load
    def make_trait(self, data, **kwargs):
        return TraitModel(**data)
