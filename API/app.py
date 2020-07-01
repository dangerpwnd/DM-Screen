from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///player.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'DMrules'
api = Api(app)

# Flask decorator
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
