from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class SpellTypeModel(Base):

    __tablename__ = "SpellType"

    # Columns
    id_spelltype = Column(Integer, primary_key=True)
    spelltype_name = Column(String(75), nullable=False, unique=True)
    spell_id = Column(Integer, ForeignKey("spell.id_spell"))

    # Relationships
    spells = relationship("SpellModel", back_populates="spell_types")

    def __repr__(self):
        return '<Spell Type (name="%s">' % (self.spelltype_name)

    @classmethod
    def find_by_name(cls, spelltype_name: str) -> SpellTypeModel:
        return cls.query.filter_by(spelltype_name=spelltype_name).first()

    @classmethod
    def find_all(cls) -> List["SpellTypeModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
