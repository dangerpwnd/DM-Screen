from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class AlignmentModel(Base):

    __tablename__ = "Alignment"

    # Columns
    id_alignment = Column(Integer, primary_key=True)
    alignment_name = Column(String(50), nullable=False, unique=True)
    alignment_descrip = Column(String(250), nullable=False)

    def __repr__(self):
        return "<Alignment (name='%s', description='%s')>" % (
            self.alignment_name,
            self.alignment_descrip,
        )

    @classmethod
    def find_by_name(cls, alignment_name: str) -> "AlignmentModel":
        return cls.query.filter_by(alignment_name=alignment_name).first()

    @classmethod
    def find_all(cls) -> List["AlignmentModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
