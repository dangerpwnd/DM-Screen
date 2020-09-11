from marshmallow import Schema, fields, post_load
from models.character import CharacterModel


class CharacterSchema(Schema):
    id_character = fields.Integer(dump_only=True)
    character_name = fields.Str()
    character_descrip = fields.Str()
    alignment_id = fields.Integer()
    alignment = fields.Nested("AlignmentSchema")
    background_id = fields.Integer()
    background = fields.Nested("BackgroundSchema")
    eye_id = fields.Integer()
    eye = fields.Nested("EyeSchema")
    hair_id = fields.Integer()
    hair = fields.Nested("HairSchema")
    race_id = fields.Integer()
    race = fields.Nested("RaceSchema")
    skin_id = fields.Integer()
    skin = fields.Nested("SkinSchema")
    subrace_id = fields.Nested("SubRaceSchema")
    armor = fields.Nested("ArmorSchema", many=True)
    attributes = fields.Nested("CharAttributeSchema", many=True)
    classes = fields.Nested("CharClassSchema", many=True)
    coins = fields.Nested("CoinSchema", many=True)
    equipment = fields.Nested("EquipmentSchema", many=True)
    factions = fields.Nested("FactionSchema", many=True)
    feats = fields.Nested("FeatSchema", many=True)
    subclasses = fields.Nested("SubClassSchema", many=True)
    tools = fields.Nested("ToolSchema", many=True)
    weapons = fields.Nested("WeaponSchema", many=True)


@post_load
def make_character(self, data, **kwargs):
    return CharacterModel(**data)
