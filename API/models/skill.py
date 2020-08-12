from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.charclass import CharClassModel as classm


class SkillModel(Base):

    __tablename__ = "Skill"

    # Columns
    id_skill = Column(Integer, primary_key=True)
    skill_name = Column(String(75), nullable=False, unique=True)
    skill_descrip = Column(String(250), nullable=False)

    # Relationships

    classes = relationship(
        "ClassModel", secondary=classm.skill_assoc, back_populates="skills"
    )

    def __repr__(self):
        return '<skill (name="%s", descrip="%s")>' % (
            self.skill_name,
            self.skill_descrip,
        )

    @classmethod
    def find_by_name(cls, skill_name: str) -> SkillModel:
        return cls.query.filter_by(skill_name=skill_name).first()

    @classmethod
    def find_all(cls) -> List["SkillModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
