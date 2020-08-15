from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class SubraceModel(Base):

    # Set table name with class attribute
    __tablename__ = "Subrace"

    # Columns
    id_subrace = Column(Integer, primary_key=True)
    subrace_name = Column(String(50), nullable=False, unique=True)
    subrace_descrip = Column(String(250), nullable=False)

    # Association Tables
    feature_assoc = Table(
        "Subrace_has_Features",
        Base.metadata,
        Column(
            "feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True
        ),
        Column(
            "subrace_id", Integer, ForeignKey("Subrace.id_subrace"), primary_key=True
        ),
    )

    prof_assoc = Table(
        "Subrace_has_Proficiencies",
        Base.metadata,
        Column(
            "proficiency_id",
            Integer,
            ForeignKey("Proficiency.id_proficiency"),
            primary_key=True,
        ),
        Column(
            "subrace_id", Integer, ForeignKey("Subrace.id_subrace"), primary_key=True
        ),
    )

    # Relationships linked to association tables
    features = relationship(
        "FeatureModel", secondary=feature_assoc, back_populates="subraces"
    )
    proficiencies = relationship(
        "ProficiencyModel", secondary=prof_assoc, back_populates="subraces"
    )

    # Relationship to PlayerChar

    def __repr__(self):
        return "<Subrace (name='%s', description='%s')>" % (
            self.subrace_name,
            self.subrace_descrip,
        )

    @classmethod
    def find_by_name(cls, subrace_name) -> "SubraceModel":
        return cls.query.filter_by(subrace_name=subrace_name).first()

    @classmethod
    def find_all(cls) -> List["SubraceModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
