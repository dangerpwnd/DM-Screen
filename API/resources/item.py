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
            item.insert()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item, 201

    def delete(self, name):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(
            table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['descrip'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return{"message": "An error occurred updating the item"}, 500
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
