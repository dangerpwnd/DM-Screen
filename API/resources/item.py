from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item_descrip',
                        type= str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    @jwt_required
    def get(self, item_name):
        item = ItemModel.find_by_name(item_name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required
    def post(self, item_name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        if ItemModel.find_by_name(item_name):
            return {'message': "An item with name '{}' already exists.".format(item_name)}

        data = Item.parser.parse_args()

        item = ItemModel(item_name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required
    def delete(self, item_name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401
        item = ItemModel.find_by_name(item_name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}

        return {'message': 'Item not found.'}, 404

    @jwt_required
    def put(self, item_name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(item_name)

        if item is None:
            item = ItemModel(item_name, **data)
        else:
            item.item_descrip = data['item_descrip']

        item.save_to_db()

        return item.json()

class ItemList(Resource):
    @jwt_required
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}
        # could also do list(map(lambda x: x.json(), ItemModel.query.all()))
