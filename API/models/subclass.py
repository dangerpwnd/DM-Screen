from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class SubClassModel(Base):

    # Set table name with class attribute
    __tablename__ = "Subclass"

    # Columns
    id_subclass = Column(Integer, primary_key=True)
    subclass_name = Column(String(75), nullable=False, unique=True)
    subclass_descrip = Column(String(250), nullable=False)
    class_id = Column(Integer, ForeignKey("Class.id_class"))

    # Association Tables

    prof_assoc = Table(
        "Subclass_has_Proficiencies",
        Base.metadata,
        Column(
            "proficiency_id",
            Integer,
            ForeignKey("Proficiency.id_proficiency"),
            primary_key=True,
        ),
        Column(
            "subclass_id", Integer, ForeignKey("Subclass.id_subclass"), primary_key=True
        ),
    )

    feature_assoc = Table(
        "Subclass_has_Features",
        Base.metadata,
        Column(
            "feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True
        ),
        Column(
            "subclass_id", Integer, ForeignKey("Subclass.id_subclass"), primary_key=True
        ),
    )

    spell_assoc = Table(
        "Subclass_has_Spells",
        Base.metadata,
        Column("spell_id", Integer, ForeignKey("Spell.id_spell"), primary_key=True),
        Column(
            "subclass_id", Integer, ForeignKey("Subclass.id_subclass"), primary_key=True
        ),
    )

    # Relationships linked to association tables

    charclass = relationship("CharClassModel", back_populates="subclasses", cascade='all, delete, delete-orphan')

    proficiencies = relationship(
        "ProficiencyModel", secondary=prof_assoc, back_populates="subclasses"
    )

    features = relationship(
        "FeatureModel", secondary=feature_assoc, back_populates="subclasses"
    )

    spells = relationship(
        "SpellModel", secondary=spell_assoc, back_populates="subclasses"
    )

    # Relationship to PlayerChar

    def __repr__(self):
        return "<Subclass (name='%s', description='%s')>" % (
            self.subclass_name,
            self.subclass_descrip,
        )

    @classmethod
    def find_by_name(cls, subclass_name) -> "SubClassModel":
        return cls.query.filter_by(subclass_name=subclass_name).first()

    @classmethod
    def find_all(cls) -> List["SubClassModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
