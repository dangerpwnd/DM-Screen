from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.proficiency import ProficiencyModel

class ProficiencySchema(SQLAlchemySchema):
    class Meta:
        model = ProficiencyModel
    id_proficiency = auto_field(dump_only=True)
    proficiency_name = auto_field()
    proficiency_descrip = auto_field()
