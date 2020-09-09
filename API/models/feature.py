from typing import List
from db import Base, session
from models.race import RaceModel as race
from models.subrace import SubRaceModel as subrace
from models.charclass import CharClassModel as classm
from models.subclass import SubClassModel as subclass

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class FeatureModel(Base):

    __tablename__ = "Feature"

    # Columns
    id_feature = Column(Integer, primary_key=True)
    feature_name = Column(String(75), nullable=False, unique=True)
    feature_descrip = Column(String(250), nullable=False)

    # Association tables
    spell_assoc = Table(
        "Feature_has_Spells",
        Base.metadata,
        Column("spell_id", Integer, ForeignKey("Spell.id_spell"), primary_key=True),
        Column(
            "feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True
        ),
    )

    # Relationships
    races = relationship(
        "RaceModel",
        secondary=race.feature_assoc,
        back_populates="features",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    subraces = relationship(
        "SubRaceModel",
        secondary=subrace.feature_assoc,
        back_populates="features",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    classes = relationship(
        "CharClassModel",
        secondary=classm.feature_assoc,
        back_populates="features",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    subclasses = relationship(
        "SubClassModel",
        secondary=subclass.feature_assoc,
        back_populates="features",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    spells = relationship(
        "SpellModel", secondary=spell_assoc, back_populates="features"
    )

    def __repr__(self):
        return '<Feature (name="%s", descrip="%s")>' % (
            self.feature_name,
            self.feature_descrip,
        )

    @classmethod
    def find_by_name(cls, feature_name: str) -> "FeatureModel":
        return cls.query.filter_by(feature_name=feature_name).first()

    @classmethod
    def find_all(cls) -> List["FeatureModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
