from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.tool import ToolModel

class Tool(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('descrip',
                        type=str,
                        required=True,
                        help="Tools require descriptions!"
    )
    parser.add_argument('weight',
                        type=int,
                        required=True,
                        help="Tools require weight!"
    )

    @jwt_required
    def get(self, name):
        tool = ToolModel.find_by_name(name)

        if tool:
            return tool.json()
        return {"message": "Tool not found."}, 404

    @jwt_required
    def post(self, name):
        if ToolModel.find_by_name(name):
            return {"message": "Tool with name '{}' already exists.".format(name)}

        data = Tool.parser.parse_args()

        tool = ToolModel(name, **data)

        try:
            tool.save_to_db()
        except:
            return {"message": "An error occurred inserting the tool."}, 500

        return tool.json(), 201

    @jwt_required
    def delete(self, name):
        tool = ToolModel.find_by_name(name)

        if tool:
            tool.delete_from_db()
            return {"message": "Tool deleted."}

        return {"message": "Tool not found."}

    @jwt_required
    def put(self, name):
        data = Tool.parser.parse_args()

        tool = ToolModel.find_by_name(name)

        if tool is None:
            tool = ToolModel(name, **data)
        else:
            tool.descrip = data['descrip']
            tool.weight = data['weight']

        tool.save_to_db()

        return tool.json()

class ToolList(Resource):
    @jwt_required
    def get(self):
        return {'Tools': [tool.json() for tool in ToolModel.query.all()]}
