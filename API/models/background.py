from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref

from models.equipment import EquipmentModel as equipm

class BackgroundModel(Base):

    # Set table name with class attribute
    __tablename__ = "Background"

    # Columns

    id_background = Column(Integer, primary_key=True)
    background_name = Column(String(50), nullable=False, unique=True)
    background_descrip = Column(String(250), nullable=False)

    # Association Proxies of equipment collection to "equipment" attribute
    # and proficiency collection to "proficiencies" attribute

    equipment = association_proxy("background_equipment", "equipment")
    proficiencies = relationship(
        "ProficiencyAssocModel", back_populates="proficiency_backgrounds"
    )

    # Relationship to PlayerChar

    def __repr__(self):
        return "<Background (name='%s', description='%s')>" % (
            self.background_name,
            self.background_descrip,
        )

    @classmethod
    def find_by_name(cls, background_name) -> "BackgroundModel":
        return cls.query.filter_by(background_name=background_name).first()

    @classmethod
    def find_by_id(cls, id_background):
        return cls.query.filter_by(id_background=id_background).first()

    @classmethod
    def find_all(cls) -> List["BackgroundModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()


# Association Objects

class EquipAssocModel(Base):

    __tablename__ = "Background_has_Equipment"

    # Columns
    equip_id = Column(Integer, ForeignKey("Equipment.id_equip"), primary_key=True)
    background_id = Column(
        Integer, ForeignKey("Background.id_background"), primary_key=True
    )

    def __init__(self, background=None, equipment=None):
        self.background = background
        self.equipment = equipment

    # bidirectional attribute/collection of "BackgroundModel"/"background_equipment"
    background = relationship("BackgroundModel", backref=backref("background_equipment", cascade="all, delete-orphan"))

    # reference to the "EquipmentModel" object
    equipment = relationship("EquipmentModel")

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()


class ProficiencyAssocModel(Base):

    __tablename__ = "Background_has_Proficiencies"

    # Columns
    proficiency_id = Column(
        Integer, ForeignKey("Proficiency.id_proficiency"), primary_key=True
    )
    background_id = Column(
        Integer, ForeignKey("Background.id_background"), primary_key=True
    )

    # Relationships
    proficiency_backgrounds = relationship(
        "BackgroundModel", back_populates="proficiencies"
    )
    backgrounds_proficiency = relationship("ProficiencyModel", back_populates="backgrounds")

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
