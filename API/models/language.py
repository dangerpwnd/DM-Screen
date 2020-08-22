from typing import List
from db import Base, session
from models.race import RaceModel as race
from models.charclass import CharClassModel as classm

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class LanguageModel(Base):

    __tablename__ = "Language"

    # Columns
    id_language = Column(Integer, primary_key=True)
    language_name = Column(String(75), nullable=False, unique=True)
    language_descrip = Column(String(250), nullable=False)

    # Relationships
    races = relationship(
        "RaceModel", secondary=race.lang_assoc, back_populates="languages", cascade='all, delete, delete-orphan', single_parent=True,
    )

    classes = relationship(
        "CharClassModel", secondary=classm.lang_assoc, back_populates="languages", cascade='all, delete, delete-orphan', single_parent=True,
    )

    def __repr__(self):
        return '<Language (name="%s", descrip="%s")>' % (
            self.language_name,
            self.language_descrip,
        )

    @classmethod
    def find_by_name(cls, language_name: str) -> 'LanguageModel':
        return cls.query.filter_by(language_name=language_name).first()

    @classmethod
    def find_all(cls) -> List["LanguageModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
