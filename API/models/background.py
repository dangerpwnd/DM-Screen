from db import db

class BackgroundModel(db.Model):

    # Set table name with class attribute
    __tablename__ = 'Background'

    # Columns
    id_back = db.Column(db.Integer, primary_key=True)
    back_name = db.Column(db.String(50), nullable=False)
    back_descrip = db.Column(db.String(250), nullable=False)
    #Relationship to PlayerChar
    # player_char = db.relationship('PlayerCharModel', backref='background', lazy=True, uselist=False)

    def __init__(self, back_name, back_descrip):
        self.back_name = back_name
        self.back_descrip = back_descrip

    def __repr__(self):
        return f"<Background {self.back_name}, {self.back_descrip}>"

    def json(self):
        return {'name': self.back_name, 'descrip': self.back_descrip}

    @classmethod
    def find_by_name(cls, back_name):
        return cls.query.filter_by(back_name=back_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

# Helper Tables

equipment_helper = db.Table('Background_has_Equipment',
    db.Column('equipment_id', db.Integer, db.ForeignKey('Equipment.id_equipment'), primary_key=True),
    db.Column('background_id', db.Integer, db.ForeignKey('Background.id_background'), primary_key=True)
)

tool_helper = db.Table('Background_has_Tools',
    db.Column('tool_id', db.Integer, db.ForeignKey('Tool.id_tool'), primary_key=True),
    db.Column('background_id', db.Integer, db.ForeignKey('Background.id_background'), primary_key=True)
)

# proficiency_helper = db.Table('Background_has_Proficiencies',
#     db.Column('proficiency_id', db.Integer, db.ForeignKey('Proficiency.id_proficiency'), primary_key=True),
#     db.Column('background_id', db.Integer, db.ForeignKey('Background.id_background'), primary_key=True)
# )
