from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Class WeaponTypeModel(Base):

    __tablename__ = 'WeaponType'

    # Columns
    id_weapontype = Column(Integer, primary_key=True)
    weapontype_name = Column(String(75), nullable=False, unique=True)
    weapon_id = Column(Integer, ForeignKey('Weapon.id_weapon'))

    # Relationships
    weapons = relationship('WeaponModel', back_populates='weapon_types')

    def __repr__(self): '<Weapon Type (name=%s>' %
        (self.weapontype_name)

    @classmethod
    find_by_name(cls, weapontype_name: str) -> WeaponTypeModel:
        return cls.query.filter_by(weapontype_name=weapontype_name).first()

    @classmethod
    find_all(cls) -> List['WeaponTypeModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
