from flask_restful import Resource, request
from models.charclass import CharClassModel
from schemas.charclass import CharClassSchema

charclass_schema = CharClassSchema()
charclass_list_schema = CharClassSchema(many=True)


class CharClass(Resource):
    @classmethod
    def get(cls, class_name: str):
        charclass = CharClassModel.find_by_name(class_name)
        if not charclass:
            return {"message": "Character class not found"}, 404
        return charclass_schema.dump(charclass), 200

    @classmethod
    def post(cls, class_name: str):
        if CharClassModel.find_by_name(class_name):
            return (
                {
                    "message": 'A character class with name "{}" already exists.'.format(
                        class_name
                    )
                },
                400,
            )

        charclass_json = request.get_json()
        charclass_json["class_name"] = class_name

        charclass = charclass_schema.load(charclass_json)

        charclass.save_to_db()

        return charclass_schema.dump(charclass), 201

    @classmethod
    def delete(cls, class_name: str):
        charclass = CharClassModel.find_by_name(class_name)

        if charclass:
            charclass.delete_from_db()
            return {"message": "Character class deleted"}, 200

        return {"message": "Character class not found"}, 404

    @classmethod
    def put(cls, class_name: str):
        charclass_json = request.get_json()
        charclass = CharClassModel.find_by_name(class_name)

        if charclass:
            charclass.class_descrip = charclass_json["class_descrip"]
        else:
            charclass_json["class_name"] = class_name
            charclass = charclass_schema.load(charclass_json)

        charclass.save_to_db()

        return charclass_schema.dump(charclass), 200


class CharClassList(Resource):
    @classmethod
    def get(cls):
        return (
            {
                "Character classes": charclass_list_schema.dump(
                    CharClassModel.find_all()
                )
            },
            200,
        )


class ClassHasEquipment(Resource):
    @classmethod
    def post(cls, class_name: str, equip_name: str):
        equipment = EquipmentModel.find_by_name(equip_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not equipment:
            return {"message": "Equipment not found."}, 404
        if not charclass:
            return {"message": "Class not found."}, 404
        charclass.equipment.append(equipment)
        charclass.save_to_db()
        return (
            {"message": "Equipment '{}' added.".format(equipment.equip_name)},
            200,
        )


class ClassHasFeatures(Resource):
    @classmethod
    def post(cls, feature_name: str, class_name: str):
        feature = FeatureModel.find_by_name(feature_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not feature:
            return {"message": "Feature not found."}, 404
        if not charclass:
            return {"message": "Class not found."}, 404
        charclass.features.append(feature)
        charclass.save_to_db()
        return (
            {"message": "Feature '{}' added.".format(feature.feature_name)},
            200,
        )


class ClassHasProficiencies(Resource):
    @classmethod
    def post(cls, proficiency_name: str, class_name: str):
        proficiency = ProficiencyModel.find_by_name(proficiency_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not proficiency:
            return {"message": "Proficiency not found."}, 404
        if not charclass:
            return {"message": "Class not found."}, 404
        charclass.proficiencies.append(proficiency)
        charclass.save_to_db()
        return (
            {"message": "Proficiency '{}' added.".format(proficiency.proficiency_name)},
            200,
        )


class ClassHasSkills(Resource):
    @classmethod
    def post(cls, skill_name: str, class_name: str):
        skill = SkillModel.find_by_name(skill_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not skill:
            return {"message": "Skill not found."}, 404
        if not charclass:
            return {"message": "Class not found."}, 404
        charclass.skills.append(skill)
        charclass.save_to_db()
        return (
            {"message": "Skill '{}' added.".format(skill.skill_name)},
            200,
        )


class ClassHasSpells(Resource):
    @classmethod
    def post(cls, spell_name: str, class_name: str):
        spell = SpellModel.find_by_name(spell_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not spell:
            return {"message": "Spell not found."}, 404
        if not charclass:
            return {"message": "Class not found."}, 404
        charclass.spells.append(spell)
        charclass.save_to_db()
        return (
            {"message": "Spell '{}' added.".format(spell.spell_name)},
            200,
        )


# ClassHasLanguages
class ClassHasLanguages(Resource):
    @classmethod
    def post(cls, language_name: str, class_name: str):
        language = LanguageModel.find_by_name(language_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not language:
            return {"message": "Language not found."}, 404
        if not charclass:
            return {"message": "Class not found."}, 404
        charclass.languages.append(language)
        charclass.save_to_db()
        return (
            {"message": "Language '{}' added.".format(language.language_name)},
            200,
        )
