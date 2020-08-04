from db import db
from models.helper import equipment_helper, tool_helper, proficiency_helper
from models.equipment import EquipmentModel
from models.tool import ToolModel
from models.proficiency import ProficiencyModel

class BackgroundModel(db.Model):

    # Set table name with class attribute
    __tablename__ = "Background"

    # Columns
    id_background = db.Column(db.Integer, primary_key=True)
    background_name = db.Column(db.String(50), nullable=False, unique=True)
    background_descrip = db.Column(db.String(250), nullable=False)
    # Relationships linked to helper tables
    equipment = db.relationship("EquipmentModel", secondary=equipment_helper)
    tools = db.relationship("ToolModel", secondary=tool_helper)
    proficiencies = db.relationship(
        "ProficiencyModel", secondary=proficiency_helper
    )
    # Relationship to PlayerChar

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
