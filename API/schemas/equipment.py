from marshmallow import Schema, fields, post_load
from models.equipment import EquipmentModel

class EquipmentSchema(Schema):
    id_equip = fields.Integer(dump_only=True)
    equip_name = fields.Str()
    equip_descrip = fields.Str()
    equip_weight = fields.Integer()

    @post_load
    def make_equipment(self, data, **kwargs):
        return EquipmentModel(**data)
