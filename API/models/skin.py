from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class SkinModel(Base):

    __tablename__ = "Skin"

    # Columns
    id_skin = Column(Integer, primary_key=True)
    skin_color = Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return "<Skin (color='%s')>" % (self.skin_color)

    @classmethod
    def find_by_color(cls, skin_color) -> "SkinModel":
        return cls.query.filter_by(skin_color=skin_color).first()

    @classmethod
    def find_all(cls) -> List["SkinModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
