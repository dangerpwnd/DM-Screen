from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

Class SkillModel(Base):

    __tablename__ = 'Skill'

    # Columns
    id_skill = Column(Integer, primary_key=True)
    skill_name = Column(String(75), nullable=False)
    skill_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__ = '<skill (name=%s, descrip=%s)>' %
        (self.skill_name, self.skill_descrip)

    @classmethod
    find_by_name(cls, skill_name: str) -> SkillModel:
        return cls.query.filter_by(skill_name=skill_name).first()

    @classmethod
    find_all(cls) -> List['SkillModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
