from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

Class factionModel(Base):

    __tablename__ = 'Faction'

    # Columns
    id_faction = Column(Integer, primary_key=True)
    faction_name = Column(String(75), nullable=False, unique=True)
    faction_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__ = '<Faction (name=%s, descrip=%s)>' %
        (self.faction_name, self.faction_descrip)

    @classmethod
    find_by_name(cls, faction_name: str) -> FactionModel:
        return cls.query.filter_by(faction_name=faction_name).first()

    @classmethod
    find_all(cls) -> List['FactionModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
