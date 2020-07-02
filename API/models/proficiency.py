from db import db

class ProficiencyModel(db.Model):

    __tablename__ = 'Proficiency'

    # Columns
    id_proficiency = db.Column(db.Integer, primary_key=True)
    proficiency_name = db.Column(db.String(100), nullable=False)
    proficiency_descrip = db.Column(db.String(250), nullable=False)

    def __init__(self, name, descrip):
        self.name = proficiency_name
        self.descrip = proficiency_descrip

    def json(self):
        return {"name": self.name, "descrip": self.descrip}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM Equipment WHERE name=name LIMIT 1

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
