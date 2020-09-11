from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class EyeModel(Base):

    __tablename__ = "Eye"

    # Columns
    id_eye = Column(Integer, primary_key=True)
    eye_color = Column(String(50), nullable=False, unique=True)

    # Relationships
    character = relationship("PlayerModel", backref="eye_color")

    def __repr__(self):
        return "<Eye (color='%s')>" % (self.eye_color)

    @classmethod
    def find_by_color(cls, eye_color) -> "EyeModel":
        return cls.query.filter_by(eye_color=eye_color).first()

    @classmethod
    def find_all(cls) -> List["EyeModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
