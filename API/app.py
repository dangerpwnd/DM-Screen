from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

import db
from blacklist import BLACKLIST

from resources.alignment import Alignment, AlignmentList
from resources.attribute import Attribute, AttributeList
from resources.background import Background, BackgroundList
from resources.coin import Coin, CoinList
from resources.equipment import Equipment, EquipmentList
from resources.eye import Eye, EyeList
from resources.faction import Faction, FactionList
from resources.feat import Feat, FeatList
from resources.feature import Feature, FeatureList
from resources.hair import Hair, HairList
from resources.language import Language, LanguageList
from resources.proficiency import Proficiency, ProficiencyList
from resources.race import Race, RaceList
from resources.size import Size, SizeList
from resources.skin import Skin, SkinList
from resources.tool import Tool, ToolList
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'DMRules' #app.config['JWT_SECRET_KEY']
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

api = Api(app)

@app.before_first_request
def create_player_db():
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
    return decrypted_token['jti'] in BLACKLIST

# Alignments
api.add_resource(Alignment, '/alignment/<string:alignment_name>')
api.add_resource(AlignmentList, '/alignments')

# Attributes
api.add_resource(Attribute, '/alignment/<string:attribute_name>')
api.add_resource(AttributeList, '/attributes')

# Backgrounds
api.add_resource(Background, '/background/<string:background_name>')
api.add_resource(BackgroundList, '/backgrounds')

# Coins
api.add_resource(Coin, '/coin/<string:coin_name>')
api.add_resource(CoinList, '/coins')

# Equipment
api.add_resource(Equipment, '/equipment/<string:equip_name>')
api.add_resource(EquipmentList, '/equipment')

# Eye Color
api.add_resource(Eye, '/eye/<string:eye_color>')
api.add_resource(EyeList, '/eyes')

# Factions
api.add_resource(Faction, '/faction/<string:faction_name>')
api.add_resource(FactionList, '/factions')

# Feats
api.add_resource(Feat, '/feat/<string:feat_name>')
api.add_resource(FeatList, '/feats')

# Features
api.add_resource(Feature, '/feature/<string:feature_name>')
api.add_resource(FeatureList, '/features')

# Hair Color
api.add_resource(Hair, '/hair/<string:hair_color>')
api.add_resource(HairList, '/hairs')

# Languages
api.add_resource(Language, '/language/<string:language_name>')
api.add_resource(LanguageList, '/languages')

# Proficiencies
api.add_resource(Proficiency, '/proficiency/<string:proficiency_name>')
api.add_resource(ProficiencyList, '/proficiencies')

# Races
api.add_resource(Race, '/race/<string:race_name>')
api.add_resource(RaceList, '/races')

# Size
api.add_resource(Size, '/size/<string:size_name>')
api.add_resource(SizeList, '/sizes')

# Skills
api.add_resource(Skill, '/skill/<string:skill_name')
api.add_resource(SkillList, '/skills')

# Skin Color
api.add_resource(Skin, '/skin/<string:skin_color>')
api.add_resource(SkinList, '/skins')

# Tools
api.add_resource(Tool, '/tool/<string:tool_name>')
api.add_resource(ToolList, '/tools')

# User Registration
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    app.run(debug=True)
