from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship


class FactionModel(Base):

    __tablename__ = "Faction"

    # Columns
    id_faction = Column(Integer, primary_key=True)
    faction_name = Column(String(75), nullable=False, unique=True)
    faction_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__(self):
        '<Faction (name="%s", descrip="%s")>' % (
            self.faction_name,
            self.faction_descrip,
        )

    @classmethod
    def find_by_name(cls, faction_name: str) -> "FactionModel":
        return cls.query.filter_by(faction_name=faction_name).first()

    @classmethod
    def find_all(cls) -> List["FactionModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
