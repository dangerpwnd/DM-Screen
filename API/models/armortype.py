from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Class ArmorTypeModel(Base):

    __tablename__ = 'Armortype'

    # Columns
    id_armortype = Column(Integer, primary_key=True)
    armortype_name = Column(String(75), nullable=False, unique=True)
    armor_id = Column(Integer, ForeignKey('Armor.id_armor'))

    # Relationships
    armor = relationship('ArmorModel', back_populates='armor_types')

    def __repr__(self): '<Armor Type (name="%s">' %
        (self.armortype_name)

    @classmethod
    find_by_name(cls, armortype_name: str) -> ArmortypeModel:
        return cls.query.filter_by(armortype_name=armortype_name).first()

    @classmethod
    find_all(cls) -> List['ArmortypeModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
