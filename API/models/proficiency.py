from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ProficiencyModel(Base):

    __tablename__ = "Proficiency"

    # Columns
    id_proficiency = Column(Integer, primary_key=True)
    proficiency_name = Column(String(100), nullable=False, unique=True)
    proficiency_descrip = Column(String(250), nullable=False)

    def __repr__(self):
        return "<Proficiency (name='%s', description='%s')>" % (
            self.proficiency_name,
            self.proficiency_descrip,
        )

    @classmethod
    def find_by_name(cls, proficiency_name) -> "ProficiencyModel":
        return cls.query.filter_by(
            proficiency_name=proficiency_name
        ).first()  # SELECT * FROM Equipment WHERE name=name LIMIT 1

    @classmethod
    def find_by_id(cls, id_proficiency):
        return cls.query.filter_by(id_proficiency=id_proficiency).first()

    @classmethod
    def find_all(cls) -> List["ProficiencyModel"]:
        return cls.query.all()

    def save_to_db(self):  # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
