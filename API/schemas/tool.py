from marshmallow import Schema, fields, post_load
from models.tool import ToolModel


class ToolSchema(Schema):
    id_tool = fields.Integer(dump_only=True)
    tool_name = fields.Str()
    tool_descrip = fields.Str()
    tool_weight = fields.Integer()

    @post_load
    def make_tool(self, data, **kwargs):
        return ToolModel(**data)
