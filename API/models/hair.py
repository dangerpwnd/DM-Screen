from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class HairModel(Base):

    __tablename__ = "Hair"

    # Columns
    id_hair = Column(Integer, primary_key=True)
    hair_color = Column(String(50), nullable=False, unique=True)

    # Relationships
    character = relationship("CharacterModel", backref="hair_color")

    def __repr__(self):
        return "<Hair (color='%s')>" % (self.hair_color)

    @classmethod
    def find_by_color(cls, hair_color) -> "HairModel":
        return cls.query.filter_by(hair_color=hair_color).first()

    @classmethod
    def find_all(cls) -> List["HairModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
