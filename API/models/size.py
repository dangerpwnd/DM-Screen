from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class SizeModel(Base):

    __tablename__ = "Size"

    # Columns
    id_size = Column(Integer, primary_key=True)
    size_name = Column(String(50), nullable=False, unique=True)

    races = relationship("Race", back_populates="size")

    def __repr__(self):
        return "<Size (name='%s')>" % (self.size_name)

    @classmethod
    def find_by_name(cls, size_name) -> "SizeModel":
        return cls.query.filter_by(size_name=size_name).first()

    @classmethod
    def find_all(cls) -> List["SizeModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
