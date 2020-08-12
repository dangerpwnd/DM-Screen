from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ArmorModel(Base):

    __tablename__ = 'Armor'

    # Columns
    id_armor = Column(Integer, primary_key=True)
    armor_name = Column(String(75), nullable=False, unique=True)
    armor_descrip = Column(String(250), nullable=False)
    armor_ac = Column(Integer, nullable=False)
    armor_weight = Column(Integer, nullable=False)
    armor_maxdex = Column(Integer, nullable=False)

    # Relationships
    armor_types = relationship('ArmorTypeModel', back_populates='armor')

    def __repr__(self): '<armor (name=%s, descrip=%s, AC=%s, weight=%s, Max Dex=%s)>' %
        (self.armor_name, self.armor_descrip, self.armor_ac, self.armor_weight, self.armor_maxdex)

    @classmethod
    find_by_name(cls, armor_name: str) -> ArmorModel:
        return cls.query.filter_by(armor_name=armor_name).first()

    @classmethod
    find_all(cls) -> List['ArmorModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
