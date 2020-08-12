from flask_restful import Resource, request
from models.spell import SpellTypeModel
from schemas.spell import SpellTypeSchema

spelltype_schema = SpellTypeSchema()
spelltype_list_schema = SpellTypeSchema(many=True)

class SpellType(Resource):

    @classmethod
    def get(cls, spelltype_name: str):
        spelltype = SpellTypeModel.find_by_name(spelltype_name)
        if not spelltype:
            return {'message': 'Spell type not found.'}, 404
        return spelltype_schema.dump(spelltype), 200

    @classmethod
    def post(cls, spelltype_name: str):
        if SpellTypeModel.find_by_name(spelltype_name):
            return {'message': 'Spell type with name "{}" already exists.'.format(spelltype_name)}

        spelltype_json = request.get_json()
        spelltype_json['spelltype_name'] = spelltype_name

        spelltype = spelltype_schema.load(spelltype_json)
        spelltype.save_to_db()
        return spelltype_schema.dump(skill), 201

    @classmethod
    def delete(cls, spelltype_name: str):
        spelltype = SpellTypeModel.find_by_name(spelltype_name)
        if spelltype:
            spelltype.delete_from_db()
            return {'message': 'Spell type deleted.'}, 200

        return {'message': 'Spell type not found.'}, 404

    # Put method not needed as only single attribute

class SpellTypeList(Resource):

    @classmethod
    def get(cls):
        return {'Spell Types': spelltype_list_schema.dump(SpellTypeModel.find_all())}
