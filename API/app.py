import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

import db
from blacklist import BLACKLIST

from resources.armor import Armor, ArmorList
from resources.armortype import ArmorType, ArmorTypeList
from resources.alignment import Alignment, AlignmentList
from resources.background import (
    Background,
    BackgroundList,
    BackgroundHasEquipment,
    BackgroundHasProficiencies,
)
from resources.coin import Coin, CoinList
from resources.charattribute import CharAttribute, CharAttributeList
from resources.charclass import (
    CharClass,
    CharClassList,
    ClassHasEquipment,
    ClassHasFeatures,
    ClassHasSkills,
    ClassHasSpells,
    ClassHasLanguages,
)
from resources.equipment import Equipment, EquipmentList
from resources.eye import Eye, EyeList
from resources.faction import Faction, FactionList
from resources.feat import Feat, FeatList, FeatHasProficiencies
from resources.feature import Feature, FeatureList
from resources.hair import Hair, HairList
from resources.language import Language, LanguageList
from resources.proficiency import Proficiency, ProficiencyList
from resources.race import (
    Race,
    RaceList,
    RaceHasFeatures,
    RaceHasLanguages,
    RaceHasProficiencies,
    RaceHasSubraces,
)
from resources.size import Size, SizeList
from resources.skill import Skill, SkillList
from resources.skin import Skin, SkinList
from resources.spell import Spell, SpellList
from resources.spelltype import SpellType, SpellTypeList
from resources.subclass import (
    SubClass,
    SubClassList,
    SubClassHasFeatures,
    SubClassHasProficiencies,
    SubClassHasSpells,
)
from resources.subrace import (
    SubRace,
    SubRaceList,
    SubRaceHasFeatures,
    SubRaceHasProficiencies,
)
from resources.tool import Tool, ToolList
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.weapon import Weapon, WeaponList
from resources.weapontype import WeaponType, WeaponTypeList

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "DMRules"  # app.config['JWT_SECRET_KEY']
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]

api = Api(app)


@app.before_first_request
def create_player_db():
    if os.path.exists("player.db"):
        os.remove("player.db")
    db.init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


# Armor
api.add_resource(Armor, "/armor/<string:armor_name>")
api.add_resource(ArmorList, "/armor")

# Armor Types
api.add_resource(ArmorType, "/armortype/<string:armortype_name>")
api.add_resource(ArmorTypeList, "/armortypes")

# Alignments
api.add_resource(Alignment, "/alignment/<string:alignment_name>")
api.add_resource(AlignmentList, "/alignments")

# Backgrounds
api.add_resource(Background, "/background/<string:background_name>")
api.add_resource(BackgroundList, "/backgrounds")
api.add_resource(
    BackgroundHasEquipment,
    "/background/<string:background_name>/equipment/<string:equip_name>",
)
api.add_resource(
    BackgroundHasProficiencies,
    "/background/<string:background_name>/proficiency/<string:proficiency_name>",
)

# Character Attributes
api.add_resource(CharAttribute, "/charattribute/<string:attribute_name>")
api.add_resource(CharAttributeList, "/charattributes")

# Character Classes
api.add_resource(CharClass, "/charclass/<string:class_name>")
api.add_resource(CharClassList, "/charclasses")
api.add_resource(
    ClassHasEquipment, "/class/<string:class_name>/equipment/<string:equip_name>"
)
api.add_resource(
    ClassHasFeatures, "/class/<string:class_name>/feature/<string:feature_name>"
)
api.add_resource(
    ClassHasLanguages, "/class/<string:class_name>/language/<string:language_name>"
)
api.add_resource(
    ClassHasProficiencies,
    "/class/<string:class_name>/proficiency/<string:proficiency_name>",
)
api.add_resource(ClassHasSkills, "/class/<string:class_name>/skill/<string:skill_name>")
api.add_resource(ClassHasSpells, "/class/<string:class_name>/spell/<string:spell_name>")

# Coins
api.add_resource(Coin, "/coin/<string:coin_name>")
api.add_resource(CoinList, "/coins")

# Equipment
api.add_resource(Equipment, "/equipment/<string:equip_name>")
api.add_resource(EquipmentList, "/equipment")

# Eye Color
api.add_resource(Eye, "/eye/<string:eye_color>")
api.add_resource(EyeList, "/eyes")

# Factions
api.add_resource(Faction, "/faction/<string:faction_name>")
api.add_resource(FactionList, "/factions")

# Feats
api.add_resource(Feat, "/feat/<string:feat_name>")
api.add_resource(FeatList, "/feats")
api.add_resource(
    FeatHasProficiencies,
    "/feat/<string:feat_name>/proficiency/<string:proficiency_name>",
)

# Features
api.add_resource(Feature, "/feature/<string:feature_name>")
api.add_resource(FeatureList, "/features")

# Hair Color
api.add_resource(Hair, "/hair/<string:hair_color>")
api.add_resource(HairList, "/hairs")

# Languages
api.add_resource(Language, "/language/<string:language_name>")
api.add_resource(LanguageList, "/languages")

# Proficiencies
api.add_resource(Proficiency, "/proficiency/<string:proficiency_name>")
api.add_resource(ProficiencyList, "/proficiencies")

# Races
api.add_resource(Race, "/race/<string:race_name>")
api.add_resource(RaceList, "/races")
api.add_resource(
    RaceHasFeatures, "/race/<string:race_name>/feature/<string:feature_name>"
)
api.add_resource(
    RaceHasLanguages, "/race/<string:race_name>/language/<string:language_name>"
)
api.add_resource(
    RaceHasProficiencies,
    "/race/<string:race_name>/proficiency/<string:proficiency_name>",
)
api.add_resource(
    RaceHasSubraces, "/race/<string:race_name>/subrace/<string:subrace_name>",
)

# Size
api.add_resource(Size, "/size/<string:size_name>")
api.add_resource(SizeList, "/sizes")

# Skills
api.add_resource(Skill, "/skill/<string:skill_name>")
api.add_resource(SkillList, "/skills")

# Skin Color
api.add_resource(Skin, "/skin/<string:skin_color>")
api.add_resource(SkinList, "/skins")

# Spells
api.add_resource(Spell, "/spell/<string:spell_name>")
api.add_resource(SpellList, "/spells")

# Spell Types
api.add_resource(SpellType, "/spelltype/<string:spelltype_name>")
api.add_resource(SpellTypeList, "/spelltypes")

# Subclasses
api.add_resource(SubClass, "/subclass/<string:subclass_name>")
api.add_resource(SubClassList, "/subclasses")
api.add_resource(
    SubClassHasFeatures,
    "/subclass/<string:subclass_name>/feature/<string:feature_name>",
)
api.add_resource(
    SubClassHasProficiencies,
    "/subclass/<string:subclass_name>/proficiency/<string:proficiency_name>",
)
api.add_resource(
    SubClassHasSpells, "/subclass/<string:subclass_name>/spell/<string:spell_name>"
)

# Subraces
api.add_resource(SubRace, "/subrace/<string:subrace_name>")
api.add_resource(SubRaceList, "/subraces")
api.add_resource(
    SubRaceHasFeatures, "/subrace/<string:subrace_name>/feature/<string:feature_name>",
)
api.add_resource(
    SubRaceHasProficiencies,
    "/subrace/<string:subrace_name>/proficiency/<string:proficiency_name>",
)

# Tools
api.add_resource(Tool, "/tool/<string:tool_name>")
api.add_resource(ToolList, "/tools")

# User Registration
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")
api.add_resource(TokenRefresh, "/refresh")

# Weapons
api.add_resource(Weapon, "/weapon/<string:weapon_name>")
api.add_resource(WeaponList, "/weapons")

# Weapon Types
api.add_resource(WeaponType, "/weapontype/<string:weapontype_name>")
api.add_resource(WeaponTypeList, "/weapontypes")

if __name__ == "__main__":
    app.run(debug=True)
