from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class RaceModel(Base):

    __tablename__ = "Race"

    # Columns
    id_race = Column(Integer, primary_key=True)
    race_name = Column(String(75), nullable=False, unique=True)
    race_descrip = Column(String(250), nullable=False)
    race_min_age = Column(Integer, nullable=False)
    race_max_age = Column(Integer, nullable=False)
    race_min_height = Column(Integer, nullable=False)
    race_max_height = Column(Integer, nullable=False)
    race_speed = Column(Integer, nullable=False)
    size_id = Column(Integer, ForeignKey("Size.id_size"))

    # Association tables

    prof_assoc = Table(
        "Race_has_Proficiencies",
        Base.metadata,
        Column(
            "proficiency_id",
            Integer,
            ForeignKey("Proficiency.id_proficiency"),
            primary_key=True,
        ),
        Column("race_id", Integer, ForeignKey("Race.id_race"), primary_key=True),
    )
    feature_assoc = Table(
        "Race_has_Features",
        Base.metadata,
        Column(
            "feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True
        ),
        Column("race_id", Integer, ForeignKey("Race.id_race"), primary_key=True),
    )
    lang_assoc = Table(
        "Race_has_Languages",
        Base.metadata,
        Column(
            "language_id", Integer, ForeignKey("Language.id_language"), primary_key=True
        ),
        Column("race_id", Integer, ForeignKey("Race.id_race"), primary_key=True),
    )

    # Relationships

    size = relationship("SizeModel", back_populates="races")
    proficiencies = relationship(
        "ProficiencyModel", secondary=prof_assoc, back_populates="races"
    )
    features = relationship(
        "FeatureModel", secondary=feature_assoc, back_populates="races"
    )
    languages = relationship(
        "LanguageModel", secondary=lang_assoc, back_populates="races"
    )

    def __repr__(self):
        return (
            "<Race (name = '%s', description = '%s', age = '%s'-'%s', height = '%s'-'%s')>"
            % (
                self.race_name,
                self.race_descrip,
                self.race_min_age,
                self.race_max_age,
                self.race_min_height,
                self.race_max_height,
            )
        )

    @classmethod
    def find_by_name(cls, race_name: str) -> 'RaceModel':
        return cls.query.filter_by(race_name=race_name).first()

    @classmethod
    def find_all(cls) -> List["RaceModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
