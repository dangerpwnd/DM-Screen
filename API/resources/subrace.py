from flask_restful import Resource, request
from models.subrace import SubraceModel
from schemas.subrace import SubraceSchema

subrace_schema = SubraceSchema()
subrace_list_schema = SubraceSchema(many=True)

class Subrace(Resource):

    @classmethod
    def get(cls, subrace_name: str):
        subrace = SubraceModel.find_by_name(subrace_name)
        if not subrace:
            return {'message': 'Subrace not found'}, 404
        return subrace_schema.dump(subrace), 200

    @classmethod
    def post(cls, subrace_name: str):
        if SubraceModel.find_by_name(subrace_name):
            return {'message': 'A subrace with name "{}" already exists.'.format(subrace_name)}, 400

        subrace_json = request.get_json()
        subrace_json['subrace_name'] = subrace_name

        subrace = subrace_schema.load(subrace_json)

        subrace.save_to_db()

        return subrace_schema.dump(subrace), 201

    @classmethod
    def delete(cls, subrace_name: str):
        subrace = SubraceModel.find_by_name(subrace_name)

        if subrace:
            subrace.delete_from_db()
            return {'message': 'Subrace deleted'}, 200

        return {'message': 'Subrace not found'}, 404

    @classmethod
    def put(cls, subrace_name: str):
        subrace_json = request.get_json()
        subrace = subraceModel.find_by_name(subrace_name)

        if subrace:
            subrace.subrace_descrip = subrace_json['subrace_descrip']
        else:
            subrace_json['subrace_name'] = subrace_name
            subrace = subrace_schema.load(subrace_json)

        subrace.save_to_db()

        return subrace_schema.dump(subrace), 200

class SubraceList(Resource):

    @classmethod
    def get(cls):
        return {'Subraces': subrace_list_schema.dump(SubraceModel.find_all())}, 200
