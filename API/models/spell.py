from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from models.feature import FeatureModel as feature
from models.charclass import CharClassModel as charclass
from models.subclass import SubClassModel as subclass


class SpellModel(Base):

    __tablename__ = "Spell"

    # Columns
    id_spell = Column(Integer, primary_key=True)
    spell_name = Column(String(75), nullable=False, unique=True)
    spell_descrip = Column(String(250), nullable=False)
    spell_amount = Column(String(25), nullable=False)
    is_racial = Column(Boolean, nullable=False)

    # Relationships
    spell_types = relationship("SpellTypeModel", back_populates="spells")
    features = relationship(
        "FeatureModel", secondary=feature.spell_assoc, back_populates="spells", cascade='all, delete, delete-orphan'
    )
    classes = relationship(
        "CharClassModel", secondary=charclass.spell_assoc, back_populates="spells", cascade='all, delete, delete-orphan'
    )
    subclasses = relationship(
        "SubClassModel", secondary=subclass.spell_assoc, back_populates="spells", cascade='all, delete, delete-orphan'
    )

    def __repr__(self):
        return '<Spell (name="%s", descrip="%s", damage="%s")>' % (
            self.spell_name,
            self.spell_descrip,
            self.spell_amount,
        )

    @classmethod
    def find_by_name(cls, spell_name: str) -> 'SpellModel':
        return cls.query.filter_by(spell_name=spell_name).first()

    @classmethod
    def find_all(cls) -> List["SpellModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
