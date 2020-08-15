from flask_restful import Resource, request
from models.subclass import SubClassModel
from schemas.subclass import SubClassSchema

subclass_schema = SubClassSchema()
subclass_list_schema =SubClassSchema(many=True)

class SubClass(Resource):

    @classmethod
    def get(cls, subclass_name: str):
        subclass = SubClassModel.find_by_name(subclass_name)
        if not subclass:
            return {'message': 'Subclass not found'}, 404
        return subclass_schema.dump(subclass), 200

    @classmethod
    def post(cls, subclass_name: str):
        if SubClassModel.find_by_name(subclass_name):
            return {'message': 'A subclass with name "{}" already exists.'.format(subclass_name)}, 400

        subclass_json = request.get_json()
        subclass_json['subclass_name'] = subclass_name

        subclass = subclass_schema.load(subclass_json)

        subclass.save_to_db()

        return subclass_schema.dump(subclass), 201

    @classmethod
    def delete(cls, subclass_name: str):
        subclass = SubClassModel.find_by_name(subclass_name)

        if subclass:
            subclass.delete_from_db()
            return {'message': 'Subclass deleted'}, 200

        return {'message': 'Subclass not found'}, 404

    @classmethod
    def put(cls, subclass_name: str):
        subclass_json = request.get_json()
        subclass = SubClassModel.find_by_name(subclass_name)

        if subclass:
            subclass.subclass_descrip = subclass_json['subclass_descrip']
        else:
            subclass_json['subclass_name'] = subclass_name
            subclass = subclass_schema.load(subclass_json)

        subclass.save_to_db()

        return subclass_schema.dump(subclass), 200

class SubClassList(Resource):

    @classmethod
    def get(cls):
        return {'Subclasses': subclass_list_schema.dump(SubClassModel.find_all())}, 200
