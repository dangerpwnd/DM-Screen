from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.equipment import EquipmentModel

class EquipmentSchema(SQLAlchemySchema):
    class Meta:
        model = EquipmentModel
    id_equipment = auto_field(dump_only=True)
    equip_name = auto_field()
    equip_descrip = auto_field()
    equip_weight = auto_field()
