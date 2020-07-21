from db import db

class ProficiencyModel(db.Model):

    __tablename__ = 'Proficiency'

    # Columns
    id_proficiency = db.Column(db.Integer, primary_key=True)
    proficiency_name = db.Column(db.String(100), nullable=False)
    proficiency_descrip = db.Column(db.String(250), nullable=False)

    def __init__(self, proficiency_name, proficiency_descrip):
        self.proficiency_name = proficiency_name
        self.proficiency_descrip = proficiency_descrip

    def json(self):
        return {"name": self.proficiency_name, "descrip": self.proficiency_descrip}

    def __repr__(self):
        return f"<Proficiency {self.proficiency_name}, {self.proficiency_descrip}>""

    @classmethod
    def find_by_name(cls, proficiency_name):
        return cls.query.filter_by(proficiency_name=proficiency_name).first() # SELECT * FROM Equipment WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
