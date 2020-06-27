from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity

from resources.item import Item, ItemList
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/RegisterUser')

if __name__ == '__main__':
    app.run(debug=True)
