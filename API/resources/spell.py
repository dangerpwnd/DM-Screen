from flask_restful import Resource, request
from models.spell import SpellModel
from schemas.spell import SpellSchema

spell_schema = SpellSchema()
spell_list_schema = SpellSchema(many=True)


class Spell(Resource):
    @classmethod
    def get(cls, spell_name: str):
        spell = SpellModel.find_by_name(spell_name)
        if not spell:
            return {"message": "Spell not found."}, 404
        return spell_schema.dump(spell), 200

    @classmethod
    def post(cls, spell_name: str):
        if SpellModel.find_by_name(spell_name):
            return {
                "message": 'Spell with name "{}" already exists.'.format(spell_name)
            }

        spell_json = request.get_json()
        spell_json["spell_name"] = spell_name

        spell = spell_schema.load(spell_json)
        spell.save_to_db()
        return spell_schema.dump(spell), 201

    @classmethod
    def delete(cls, spell_name: str):
        spell = SpellModel.find_by_name(spell_name)
        if spell:
            spell.delete_from_db()
            return {"message": "Spell deleted."}, 200

        return {"message": "Spell not found."}, 404

    @classmethod
    def put(cls, spell_name: str):
        spell_json = request.get_json()
        spell = SpellModel.find_by_name(spell_name)

        if spell:
            spell.spell_descrip = spell_json["spell_descrip"]
            spell.spell_amount = spell_json["spell_amount"]
            spell.spelltype_id = spell_json["spelltype_id"]
        else:
            spell_json["spell_name"] = spell_name
            spell = spell_schema.load(spell_json)

        spell.save_to_db()

        return spell_schema.dump(spell), 200


class SpellList(Resource):
    @classmethod
    def get(cls):
        return {"Spells": spell_list_schema.dump(SpellModel.find_all())}
