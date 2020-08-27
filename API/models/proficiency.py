from typing import List
from db import Base, session
from models.race import RaceModel as race
from models.subrace import SubRaceModel as subrace
from models.charclass import CharClassModel as classm
from models.subclass import SubClassModel as subclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ProficiencyModel(Base):

    __tablename__ = "Proficiency"

    # Columns
    id_proficiency = Column(Integer, primary_key=True)
    proficiency_name = Column(String(100), nullable=False, unique=True)
    proficiency_descrip = Column(String(250), nullable=False)

    backgrounds = relationship(
        "ProficiencyAssocModel",
        back_populates="backgrounds_proficiency",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    races = relationship(
        "RaceModel",
        secondary=race.prof_assoc,
        back_populates="proficiencies",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    subraces = relationship(
        "SubRaceModel",
        secondary=subrace.prof_assoc,
        back_populates="proficiencies",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    classes = relationship(
        "CharClassModel",
        secondary=classm.prof_assoc,
        back_populates="proficiencies",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    subclasses = relationship(
        "SubClassModel",
        secondary=subclass.prof_assoc,
        back_populates="proficiencies",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    def __repr__(self):
        return "<Proficiency (name='%s', description='%s')>" % (
            self.proficiency_name,
            self.proficiency_descrip,
        )

    @classmethod
    def find_by_name(cls, proficiency_name) -> "ProficiencyModel":
        return cls.query.filter_by(
            proficiency_name=proficiency_name
        ).first()  # SELECT * FROM Equipment WHERE name=name LIMIT 1

    @classmethod
    def find_by_id(cls, id_proficiency):
        return cls.query.filter_by(id_proficiency=id_proficiency).first()

    @classmethod
    def find_all(cls) -> List["ProficiencyModel"]:
        return cls.query.all()

    def save_to_db(self):  # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
