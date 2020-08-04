from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.tool import ToolModel

class ToolSchema(SQLAlchemySchema):
    class Meta:
        model = ToolModel
    id_tool = auto_field(dump_only=True)
    tool_name = auto_field()
    tool_descrip = auto_field()
    tool_weight = auto_field()
