from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Class SpellTypeModel(Base):

    __tablename__ = 'SpellType'

    # Columns
    id_spelltype = Column(Integer, primary_key=True)
    spelltype_name = Column(String(75), nullable=False, unique=True)
    spell_id = Column(Integer, ForeignKey('spell.id_spell'))

    # Relationships
    spells = relationship('SpellModel', back_populates='spell_types')

    def __repr__(self):  '<Spell Type (name="%s">' %
        (self.spelltype_name)

    @classmethod
    find_by_name(cls, spelltype_name: str) -> SpellTypeModel:
        return cls.query.filter_by(spelltype_name=spelltype_name).first()

    @classmethod
    find_all(cls) -> List['SpellTypeModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
