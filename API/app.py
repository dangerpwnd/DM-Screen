from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

import db
from blacklist import BLACKLIST

from resources.background import Background, BackgroundList
from resources.equipment import Equipment, EquipmentList
from resources.proficiency import Proficiency, ProficiencyList
from resources.race import Race, RaceList
from resources.size import Size, SizeList
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

# Backgrounds
api.add_resource(Background, '/background/<string:background_name>')
api.add_resource(BackgroundList, '/backgrounds')

# Equipment
api.add_resource(Equipment, '/equipment/<string:equip_name>')
api.add_resource(EquipmentList, '/equipment')

# Features
api.add_resource(Feature, '/feature/<string:feature_name>')
api.add_resource(FeatureList, '/features')

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
