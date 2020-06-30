from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    TABLE_NAME: 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('descrip',
                        type='text',
                        required=True,
                        help="This field cannot be left blank!"
                        )
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel{name, data['descrip']}

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = ItemModel.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['descrip'])
        else:
            item.descrip = data['descrip']

        item.save_to_db()

        return updated_item.json()

class ItemList(Resource):
    TABLE_NAME = 'items'

    @jwt_required()
    def get(self):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'descrip': row[1]})
        connection.close()

        return {'items': items}
