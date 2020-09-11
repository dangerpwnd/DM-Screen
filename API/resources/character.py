from flask_restful import Resource, request
from models.background import CharacterModel
from models.equipment import EquipmentModel
from models.proficiency import ProficiencyModel
from schemas.background import CharacterSchema

character_schema = CharacterSchema()
character_list_schema = CharacterSchema(many=True)

class Character(Resource):
    @classmethod
    def get(cls, character_name: str):
        character = CharacterModel.find_by_name(character_name)
        if not character:
            return {"message": "Character not found"}, 404
        return character_schema.dump(character), 200

    @classmethod
    def post(cls, character_name: str):
        if CharacterModel.find_by_name(character_name):
            return (
                {
                    "message": 'A character with name "{}" already exists.'.format(
                        character_name
                    )
                },
                400,
            )

        character_json = request.get_json()
        character_json["character_name"] = character_name

        character = character_schema.load(character_json)

        character.save_to_db()

        return character_schema.dump(character), 201

    @classmethod
    def delete(cls, character_name: str):
        character = CharacterModel.find_by_name(character_name)

        if character:
            character.delete_from_db()
            return {"message": "Character deleted"}, 200

        return {"message": "Character not found"}, 404

    @classmethod
    def put(cls, character_name: str):
        character_json = request.get_json()
        character = CharacterModel.find_by_name(character_name)

        if character:
            character.character_descrip = character_json["character_descrip"]
            character.alignment_id = character_json["alignment_id"]
            character.background_id = character_json["background_id"]
            character.eye_id = character_json["eye_id"]
            character.hair_id = character_json["hair_id"]
            character.race_id = character_json["race_id"]
            character.skin_id = character_json["skin_id"]
            character.subrace_id = character_json["subrace_id"]
        else:
            character_json["character_name"] = character_name
            character = character_schema.load(character_json)

        character.save_to_db()

        return character_schema.dump(character), 200


class CharacterList(Resource):
    @classmethod
    def get(cls):
        return (
            {"characters": character_list_schema.dump(CharacterModel.find_all())},
            200,
        )


class CharacterHasArmor(Resource):
    @classmethod
    def post(cls, character_name: str, armor_name: str):
        character = CharacterModel.find_by_name(character_name)
        armor = ArmorModel.find_by_name(armor_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not armor:
            return {"message": "Armor not found."}, 404
        character.armor.append(armor)
        character.save_to_db()
        return (
            {"message": "Armor '{}' added.".format(armor.armor_name)},
            200,
        )


class CharacterHasAttributes(Resource):
    @classmethod
    def post(cls, character_name: str, attribute_name: str):
        character = CharacterModel.find_by_name(character_name)
        attribute = CharAttributeModel.find_by_name(attribute_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not attribute:
            return {"message": "Attribute not found."}, 404
        character.attributes.append(attribute)
        character.save_to_db()
        return (
            {"message": "Attribute '{}' added.".format(attribute.attribute_name)},
            200,
        )

class CharacterHasClasses(Resource):
    @classmethod
    def post(cls, character_name: str, class_name: str):
        character = CharacterModel.find_by_name(character_name)
        charclass = CharClassModel.find_by_name(class_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not charclass:
            return {"message": "Character class not found."}, 404
        character.classes.append(charclass)
        character.save_to_db()
        return (
            {"message": "Character class '{}' added.".format(charclass.class_name)},
            200,
        )

class CharacterHasCoins(Resource):
    @classmethod
    def post(cls, character_name: str, coin_name: str):
        character = CharacterModel.find_by_name(character_name)
        coin = CoinModel.find_by_name(coin_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not coin:
            return {"message": "Coin not found."}, 404
        character.coins.append(coin)
        character.save_to_db()
        return (
            {"message": "Coin '{}' added.".format(coin.coin_name)},
            200,
        )

class CharacterHasEquipment(Resource):
    @classmethod
    def post(cls, character_name: str, equip_name: str):
        character = CharacterModel.find_by_name(character_name)
        equipment = EquipmentModel.find_by_name(equip_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not equipment:
            return {"message": "Equipment not found."}, 404
        character.equipment.append(equipment)
        character.save_to_db()
        return (
            {"message": "Equipment '{}' added.".format(equipment.equip_name)},
            200,
        )

class CharacterHasFactions(Resource):
    @classmethod
    def post(cls, character_name: str, faction_name: str):
        character = CharacterModel.find_by_name(character_name)
        faction = FactionModel.find_by_name(faction_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not faction:
            return {"message": "Faction not found."}, 404
        character.factions.append(faction)
        character.save_to_db()
        return (
            {"message": "Faction '{}' added.".format(faction.faction_name)},
            200,
        )

class CharacterHasFeats(Resource):
    @classmethod
    def post(cls, character_name: str, feat_name: str):
        character = CharacterModel.find_by_name(character_name)
        feat = FeatModel.find_by_name(feat_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not feat:
            return {"message": "Feat not found."}, 404
        character.feats.append(feat)
        character.save_to_db()
        return (
            {"message": "Feat '{}' added.".format(feat.feat_name)},
            200,
        )

class CharacterHaSubclasses(Resource):
    @classmethod
    def post(cls, character_name: str, subclass_name: str):
        character = CharacterModel.find_by_name(character_name)
        subclass = SubClassModel.find_by_name(subclass_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not subclass:
            return {"message": "Subclass not found."}, 404
        character.subclasses.append(subclass)
        character.save_to_db()
        return (
            {"message": "Subclass '{}' added.".format(subclass.subclass_name)},
            200,
        )

class CharacterHasTools(Resource):
    @classmethod
    def post(cls, character_name: str, tool_name: str):
        character = CharacterModel.find_by_name(character_name)
        tool = ToolModel.find_by_name(tool_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not tool:
            return {"message": "Tool not found."}, 404
        character.tools.append(tool)
        character.save_to_db()
        return (
            {"message": "Tool '{}' added.".format(tool.tool_name)},
            200,
        )

class CharacterHasWeapons(Resource):
    @classmethod
    def post(cls, character_name: str, weapon_name: str):
        character = CharacterModel.find_by_name(character_name)
        weapon = WeaponModel.find_by_name(weapon_name)
        if not character:
            return {"message": "Character not found."}, 404
        if not weapon:
            return {"message": "Weapon not found."}, 404
        character.weapons.append(weapon)
        character.save_to_db()
        return (
            {"message": "Weapon '{}' added.".format(weapon.weapon_name)},
            200,
        )
