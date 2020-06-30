from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCEMY_DATABASE_URI'] = 'sqlite:///player.db'
app.config['SQLALCEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/RegisterUser')

if __name__ == '__main__':
    app.run(debug=True)
    db.init_app(app)
