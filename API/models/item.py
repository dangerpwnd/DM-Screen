import sqlite3

class ItemModel:
    def __init__(self, name, descrip):
        self.name = name
        self.descrip = descrip

    def json(self):
        return {'name': self.name, 'descrip': self.descrip}

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
            return cls(*row)

    def insert(self):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUE(?,?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (self.name, self.descrip))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('player.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET descrip=? WHERE name=?".format(
            table=cls.TABLE_NAME)
        cursor.execute(query, (self.descrip, self.name))

        connection.commit()
        connection.close()
