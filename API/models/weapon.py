from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Class WeaponModel(Base):

    __tablename__ = 'Weapon'

    # Columns
    id_weapon = Column(Integer, primary_key=True)
    weapon_name = Column(String(75), nullable=False, unique=True)
    weapon_descrip = Column(String(250), nullable=False)
    weapon_damage = Column(Integer, nullable=False)
    weapon_weight = Column(Integer, nullable=False)

    # Relationships
    weapon_types = relationship('WeaponTypeModel')

    def __repr__ = '<Weapon (name=%s, descrip=%s)>' %
        (self.weapon_name, self.weapon_descrip)

    @classmethod
    find_by_name(cls, weapon_name: str) -> WeaponModel:
        return cls.query.filter_by(weapon_name=weapon_name).first()

    @classmethod
    find_all(cls) -> List['WeaponModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
