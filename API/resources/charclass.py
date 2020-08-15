from flask_restful import Resource, request
from models.charclass import CharClassModel
from schemas.charclass import CharClassSchema

charclass_schema = CharClassSchema()
charclass_list_schema =CharClassSchema(many=True)

class CharClass(Resource):

    @classmethod
    def get(cls, class_name: str):
        charclass = CharClassModel.find_by_name(class_name)
        if not charclass:
            return {'message': 'Character class not found'}, 404
        return charclass_schema.dump(charclass), 200

    @classmethod
    def post(cls, class_name: str):
        if CharClassModel.find_by_name(class_name):
            return {'message': 'A character class with name "{}" already exists.'.format(class_name)}, 400

        charclass_json = request.get_json()
        charclass_json['class_name'] = class_name

        charclass = charclass_schema.load(charclass_json)

        charclass.save_to_db()

        return charclass_schema.dump(charclass), 201

    @classmethod
    def delete(cls, class_name: str):
        charclass = CharClassModel.find_by_name(class_name)

        if charclass:
            charclass.delete_from_db()
            return {'message': 'Character class deleted'}, 200

        return {'message': 'Character class not found'}, 404

    @classmethod
    def put(cls, class_name: str):
        charclass_json = request.get_json()
        charclass = CharClassModel.find_by_name(class_name)

        if charclass:
            charclass.class_descrip = charclass_json['class_descrip']
        else:
            charclass_json['class_name'] = class_name
            charclass = charclass_schema.load(charclass_json)

        charclass.save_to_db()

        return charclass_schema.dump(charclass), 200

class CharClassList(Resource):

    @classmethod
    def get(cls):
        return {'Character classes': charclass_list_schema.dump(CharClassModel.find_all())}, 200
