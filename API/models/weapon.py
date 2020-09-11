from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String, ForeignKey

class WeaponModel(Base):

    __tablename__ = "Weapon"

    # Columns
    id_weapon = Column(Integer, primary_key=True)
    weapon_name = Column(String(75), nullable=False, unique=True)
    weapon_descrip = Column(String(250), nullable=False)
    weapon_damage = Column(String(25), nullable=False)
    weapon_weight = Column(Integer, nullable=False)
    weapontype_id = Column(Integer, ForeignKey("WeaponType.id_weapontype"), nullable=False)

    def __repr__(self):
        return '<Weapon (name="%s", descrip="%s", damage="%s", weight="%s")>' % (
            self.weapon_name,
            self.weapon_descrip,
            self.weapon_damage,
            self.weapon_weight,
        )

    @classmethod
    def find_by_name(cls, weapon_name: str) -> "WeaponModel":
        return cls.query.filter_by(weapon_name=weapon_name).first()

    @classmethod
    def find_all(cls) -> List["WeaponModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
