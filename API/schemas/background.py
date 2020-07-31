from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from models.background import BackgroundModel
from schemas.equipment import EquipmentSchema
from schemas.tool import ToolSchema
from schemas.proficiency import ProficiencySchema

class BackgroundSchema(SQLAlchemySchema):
    class Meta:
        model = BackgroundModel
    id_background = auto_field(dump_only=True)
    background_name = auto_field()
    background_descrip = auto_field()
    equipment = Nested('EquipmentSchema', many=True)
    tools = Nested('ToolSchema', many=True)
    proficiencies = Nested('ProficiencySchema', many=True)
