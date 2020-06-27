from flask_restful import Resource, reqparse
import sqlite3


class Item(Resource):
    TABLE_NAME: 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('descrip',
                        type='text',
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(
            table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'descrip': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = {'name': name, 'descrip': data['descrip']}

        try:
            Item.insert(item)
        except:
            return {"message": "An error occurred inserting the item."}

        return item

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUE(?,?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'], item['descrip']))

        connection.commit()
        connection.close()

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
        item = self.find_by_name(name)
        updated_item = {'name': name, 'descrip': data['descrip']}
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item"}
        else:
            try:
                Item.update(updated_item)
            except:
                return{"message": "An error occurred updating the item"}
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET descrip=? WHERE name=?".format(
            table=cls.TABLE_NAME)
        cursor.execute(query, (item['descrip'], item['name']))

        connection.commit()
        connection.close()


class ItemList(Resource):
    TABLE_NAME = 'items'

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
