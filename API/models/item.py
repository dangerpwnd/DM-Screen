from db import db

class ItemModel(db.Model):

    __tablename__ = 'Items'

    id_item = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80))
    item_descrip = db.Column(db.String(80))

    def __init__(self, item_name, item_descrip):
        self.item_name = item_name
        self.item_descrip = item_descrip

    def __repr__(self):
        return f"<Item {self.item_name}, {self.item_descrip}>"

    def json(self):
        return {'name': self.item_name, 'descrip': self.item_descrip}

    @classmethod
    def find_by_name(cls, item_name):
        return cls.query.filter_by(item_name=item_name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
