from typing import List
from db import Base, session
from models.race import RaceModel as race

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class LanuageModel(Base):

    __tablename__ = 'Language'

    # Columns
    id_language = Column(Integer, primary_key=True)
    language_name = Column(String(75), nullable=False)
    language_descrip = Column(String(250), nullable=False)

    # Relationships
    races = relationship('RaceModel',
        secondary=race.lang_assoc,
        back_populates='languages')

    def __repr__ = '<Language (name=%s, descrip=%s)>' %
        (self.language_name, self.language_descrip)

    @classmethod
    find_by_name(cls, language_name: str) -> LanguageModel:
        return cls.query.filter_by(language_name=language_name).first()

    @classmethod
    find_all(cls) -> List['LanguageModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
