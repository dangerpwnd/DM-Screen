from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_claims
from models.tool import ToolModel
from schemas.tool import ToolSchema

tool_schema = ToolSchema()
tool_list_schema = ToolSchema(many=True)

class Tool(Resource):
    @jwt_required
    @classmethod
    def get(cls, name: str):
        tool = ToolModel.find_by_name(name)
        if not tool:
            return {"message": "Tool not found."}, 404
        return tool_schema.dump(tool), 200

    @jwt_required
    @classmethod
    def post(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        if ToolModel.find_by_name(name):
            return {"message": "Tool with name '{}' already exists.".format(name)}

        tool_json = request.get_json()
        tool = tool_schema.load(tool_json)

        try:
            tool.save_to_db()
        except:
            return {"message": "An error occurred inserting the tool."}, 500

        return tool_schema.dump(tool), 201

    @jwt_required
    @classmethod
    def delete(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        tool = ToolModel.find_by_name(name)

        if tool:
            tool.delete_from_db()
            return {"message": "Tool deleted."}

        return {"message": "Tool not found."}

    @jwt_required
    @classmethod
    def put(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        tool_json = request.get_json()
        tool = ToolModel.find_by_name(name)

        if tool:
            tool.tool_descrip = tool_json['tool_descrip']
            tool.tool_weight = tool_json['tool_weight']
        else:
            tool = tool_schema.load(tool_json)

        tool.save_to_db()

        return tool_schema.dump(tool), 200

class ToolList(Resource):
    @jwt_required
    @classmethod
    def get(cls):
        return {'Tools': tool_list_schema.dump(ToolModel.find_all())}
