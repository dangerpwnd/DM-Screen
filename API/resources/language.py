from flask_restful import Resource, request
from models.language import LanguageModel
from schemas.language import LanguageSchema

language_schema = LanguageSchema()
language_list_schema = LanguageSchema(many=True)

class Language(Resource):

    @classmethod
    def get(cls, language_name: str):
        language = LanguageModel.find_by_name(language_name)
        if not language:
            return {'message': 'Language not found.'}, 404
        return language_schema.dump(language), 200

    @classmethod
    def post(cls, language_name: str):
        if LanguageModel.find_by_name(language_name):
            return {'message': 'Language with name "{}" already exists.'.format(language_name)}

        language_json = request.get_json()
        language_json['language_name'] = language_name

        language = language_schema.load(language_json)
        language.save_to_db()
        return language_schema.dump(language), 201

    @classmethod
    def delete(cls, language_name: str):
        language = LanguageModel.find_by_name(language_name)
        if language:
            language.delete_from_db()
            return {'message': 'Language deleted.'}, 200

        return {'message': 'Language not found.'}, 404

    @classmethod
    def put(cls, language_name: str):
        language_json = request.get_json()
        language = LanguageModel.find_by_name(language_name)

        if language:
            language.language_descrip = language_json['language_descrip']
        else:
            language_json['language_name'] = language_name
            language = language_schema.load(language_json)

        language.save_to_db()

        return language_schema.dump(language), 200

class LanguageList(Resource):

    @classmethod
    def get(cls):
        return {'languages': language_list_schema.dump(LanguageModel.find_all())}
