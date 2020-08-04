from db import db

class PlayerModel(db.Model):

    __tablename__ = 'PlayerChar'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    descrip = db.Column(db.String(80))

    def __init__(self, name, descrip):
        self.name = name
        self.descrip = descrip

    def json(self):
        return {'name': self.name, 'descrip': self.descrip}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
