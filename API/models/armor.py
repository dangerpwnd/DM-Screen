from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.armortype import ArmorTypeModel as AType


class ArmorModel(Base):

    __tablename__ = "Armor"

    # Columns
    id_armor = Column(Integer, primary_key=True)
    armor_name = Column(String(75), nullable=False, unique=True)
    armor_descrip = Column(String(250), nullable=False)
    armor_ac = Column(Integer, nullable=False)
    armor_weight = Column(Integer, nullable=False)
    armor_maxdex = Column(Integer, nullable=False)
    armortype_id = Column(Integer, ForeignKey("ArmorType.id_armortype"), nullable=False)

    def __repr__(self):
        return (
            "<Armor (name='%s', descrip='%s', AC='%s', weight='%s', Max Dex='%s')>"
            % (
                self.armor_name,
                self.armor_descrip,
                self.armor_ac,
                self.armor_weight,
                self.armor_maxdex,
            )
        )

    @classmethod
    def find_by_name(cls, armor_name: str) -> "ArmorModel":
        return (
            cls.query.filter_by(armor_name=armor_name)
            .filter(ArmorModel.armortype_id == AType.id_armortype)
            .outerjoin(AType)
            .first()
        )

    @classmethod
    def find_all(cls) -> List["ArmorModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
