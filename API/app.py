from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow
from db import db
from blacklist import BLACKLIST

from resources.background import Background, BackgroundList
from resources.equipment import Equipment, EquipmentList
from resources.item import Item, ItemList
from resources.proficiency import Proficiency, ProficiencyList
from resources.tool import Tool, ToolList
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh

from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///player.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'DMRules' #app.config['JWT_SECRET_KEY']
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

# Marshmallow Schemas
# ma = Marshmallow(app)
#
# class BackgroundSchema(ma.Schema):
#     class Meta:
#         fields = ('id_background', 'background_name', 'background_descrip')
#

api = Api(app)

# Flask decorator
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: # Instead of hard coding, should read from config file or database
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

# Backgrounds
api.add_resource(Background, '/background/<string:background_name>')
api.add_resource(BackgroundList, '/backgrounds')

# Equipment
api.add_resource(Equipment, '/equipment/<string:equip_name>')
api.add_resource(EquipmentList, '/equipment')

# Items
api.add_resource(Item, '/item/<string:item_name>')
api.add_resource(ItemList, '/items')

# Proficiencies
api.add_resource(Proficiency, '/proficiency/<string:proficiency_name>')
api.add_resource(ProficiencyList, '/proficiencies')

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
    db.init_app(app)
    app.run(debug=True)
