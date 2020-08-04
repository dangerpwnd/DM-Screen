from db import db

class EquipmentModel(db.Model):

    __tablename__ = 'Equipment'

    # Columns
    id_equipment = db.Column(db.Integer, primary_key=True)
    equip_name = db.Column(db.String(100), nullable=False)
    equip_descrip = db.Column(db.String(250), nullable=False)
    equip_weight = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_name(cls, equip_name):
        return cls.query.filter_by(equip_name=equip_name).first() # SELECT * FROM Equipment WHERE name(table column)=name(find by name) LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
