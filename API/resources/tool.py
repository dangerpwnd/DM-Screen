from flask_restful import Resource, request
from models.tool import ToolModel
from schemas.tool import ToolSchema

tool_schema = ToolSchema()
tool_list_schema = ToolSchema(many=True)


class Tool(Resource):
    @classmethod
    def get(cls, tool_name: str):
        tool = ToolModel.find_by_name(tool_name)
        if not tool:
            return {"message": "Tool not found."}, 404
        return tool_schema.dump(tool), 200

    @classmethod
    def post(cls, tool_name: str):

        if ToolModel.find_by_name(tool_name):
            return {"message": "Tool with name '{}' already exists.".format(tool_name)}

        tool_json = request.get_json()
        tool_json["tool_name"] = tool_name

        tool = tool_schema.load(tool_json)

        tool.save_to_db()

        return tool_schema.dump(tool), 201

    @classmethod
    def delete(cls, tool_name: str):

        tool = ToolModel.find_by_name(tool_name)

        if tool:
            tool.delete_from_db()
            return {"message": "Tool deleted."}

        return {"message": "Tool not found."}

    @classmethod
    def put(cls, tool_name: str):

        tool_json = request.get_json()
        tool = ToolModel.find_by_name(tool_name)

        if tool:
            tool.tool_descrip = tool_json["tool_descrip"]
            tool.tool_weight = tool_json["tool_weight"]
        else:
            tool_json["tool_name"] = tool_name
            tool = tool_schema.load(tool_json)

        tool.save_to_db()

        return tool_schema.dump(tool), 200


class ToolList(Resource):
    @classmethod
    def get(cls):
        return {"Tools": tool_list_schema.dump(ToolModel.find_all())}
