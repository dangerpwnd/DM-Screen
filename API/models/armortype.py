from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ArmorTypeModel(Base):

    __tablename__ = "Armortype"

    # Columns
    id_armortype = Column(Integer, primary_key=True)
    armortype_name = Column(String(75), nullable=False, unique=True)
    armor_id = Column(Integer, ForeignKey("Armor.id_armor"))

    # Relationships
    armor = relationship("ArmorModel", back_populates="armor_types")

    def __repr__(self):
        return '<Armor Type (name="%s">' % (self.armortype_name)

    @classmethod
    def find_by_name(cls, armortype_name: str) -> ArmortypeModel:
        return cls.query.filter_by(armortype_name=armortype_name).first()

    @classmethod
    def find_all(cls) -> List["ArmortypeModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()