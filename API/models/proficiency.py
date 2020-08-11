from typing import List
from db import Base, session
from models.background import BackgroundModel as background
from models.race import RaceModel as race
from models.subrace import SubraceModel as subrace
from models.charclass import CharClassModel as classm
from models.subclass import SubClassModel as subclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ProficiencyModel(Base):

    __tablename__ = 'Proficiency'

    # Columns
    id_proficiency = Column(Integer, primary_key=True)
    proficiency_name = Column(String(100), nullable=False, unique=True)
    proficiency_descrip = Column(String(250), nullable=False)

    backgrounds = relationship('BackgroundModel',
                            secondary=background.prof_assoc,
                            back_populates='proficiencies')

    races = relationship('RaceModel',
                            secondary=race.prof_assoc,
                            back_populates='proficiencies')

    subraces = relationship('SubraceModel',
                                secondary=subrace.prof_assoc,
                                back_populates='proficiencies')

    classes = relationship('ClassModel',
                                  secondary=classm.prof_assoc,
                                  back_populates='proficiencies')

    subclasses = relationship('SubClassModel',
                                  secondary=subclass.feature_assoc,
                                  back_populates='proficiencies')

    def __repr__(self):
        return "<Proficiency (name='%s', description='%s')>" % (
                                        self.proficiency_name,
                                        self.proficiency_descrip)

    @classmethod
    def find_by_name(cls, proficiency_name) -> "ProficiencyModel":
        return cls.query.filter_by(proficiency_name=proficiency_name).first() # SELECT * FROM Equipment WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls) -> List["ProficiencyModel"]:
        return cls.query.all()

    def save_to_db(self): # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
