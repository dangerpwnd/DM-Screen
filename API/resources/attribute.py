from flask_restful import Resource, request
from models.attribute import AttributeModel
from schemas.attribute import AttributeSchema

attribute_schema = AttributeSchema()
attribute_list_schema = AttributeSchema(many=True)

class Attribute(Resource):

    @classmethod
    def get(cls, attribute_name: str):
        attribute = AttributeModel.find_by_name(attribute_name)
        if not attribute:
            return {'message': 'Attribute not found.'}, 404
        return attribute_schema.dump(attribute), 200

    @classmethod
    def post(cls, attribute_name: str):
        if AttributeModel.find_by_name(attribute_name):
            return {'message': 'Attribute with name "{}" already exists.'.format(attribute_name)}

        attribute_json = request.get_json()
        attribute_json['attribute_name'] = attribute_name

        attribute = attribute_schema.load(attribute_json)
        attribute.save_to_db()
        return attribute_schema.dump(attribute), 201

    @classmethod
    def delete(cls, attribute_name: str):
        attribute = AttributeModel.find_by_name(attribute_name)
        if attribute:
            attribute.delete_from_db()
            return {'message': 'Attribute deleted.'}, 200

        return {'message': 'Attribute not found.'}, 404

    @classmethod
    def put(cls, attribute_name: str):
        attribute_json = request.get_json()
        attribute = AttributeModel.find_by_name(attribute_name)

        if attribute:
            attribute.attribute_descrip = attribute_json['attribute_descrip']
        else:
            attribute_json['attribute_name'] = attribute_name
            attribute = attribute_schema.load(attribute_json)

        attribute.save_to_db()

        return attribute_schema.dump(attribute), 200

class AttributeList(Resource):

    @classmethod
    def get(cls):
        return {'Attributes': attribute_list_schema.dump(AttributeModel.find_all())}
