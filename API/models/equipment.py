from typing import List
from db import Base, session
from models.background import BackgroundModel as background
from models.charclass import CharClassModel as classm

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class EquipmentModel(Base):

    __tablename__ = 'Equipment'

    # Columns
    id_equip = Column(Integer, primary_key=True)
    equip_name = Column(String(100), nullable=False, unique=True)
    equip_descrip = Column(String(250), nullable=False)
    equip_weight = Column(Integer, nullable=False)

    backgrounds = relationship('BackgroundModel',
                                  secondary=background.equip_assoc,
                                  back_populates='equipment')

    classes = relationship('ClassModel',
                                  secondary=classm.equip_assoc,
                                  back_populates='equipment')

    def __repr__(self):
        return "<Equipment (name='%s', description='%s', weight='%s')>" % (
                                        self.equip_name,
                                        self.equip_descrip,
                                        self.equip_weight)
    @classmethod
    def find_by_name(cls, equip_name) -> "EquipmentModel":
        return cls.query.filter_by(equip_name=equip_name).first() # SELECT * FROM Equipment WHERE name(table column)=name(find by name) LIMIT 1

    @classmethod
    def find_all(cls) -> List["EquipmentModel"]:
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
