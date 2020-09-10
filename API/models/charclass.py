from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


# Association Tables
class_has_equipment = Table(
    "Class_has_Equipment",
    Base.metadata,
    Column("equip_id", Integer, ForeignKey("Equipment.id_equip"), primary_key=True),
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
)

class_has_proficiencies = Table(
    "Class_has_Proficiencies",
    Base.metadata,
    Column(
        "proficiency_id",
        Integer,
        ForeignKey("Proficiency.id_proficiency"),
        primary_key=True,
    ),
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
)

class_has_features = Table(
    "Class_has_Features",
    Base.metadata,
    Column("feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True),
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
)

class_has_skills = Table(
    "Class_has_Skills",
    Base.metadata,
    Column("skill_id", Integer, ForeignKey("Skill.id_skill"), primary_key=True),
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
)

class_has_spells = Table(
    "Class_has_Spells",
    Base.metadata,
    Column("spell_id", Integer, ForeignKey("Spell.id_spell"), primary_key=True),
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
)

class_has_languages = Table(
    "Class_has_Languages",
    Base.metadata,
    Column(
        "language_id", Integer, ForeignKey("Language.id_language"), primary_key=True
    ),
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
)


class CharClassModel(Base):

    # Set table name with class attribute
    __tablename__ = "Class"

    # Columns
    id_class = Column(Integer, primary_key=True)
    class_name = Column(String(75), nullable=False, unique=True)
    class_descrip = Column(String(250), nullable=False)

    # Relationships
    subclasses = relationship("SubClassModel", back_populates="charclass")

    equipment = relationship("EquipmentModel", secondary=lambda: class_has_equipment)

    proficiencies = relationship(
        "ProficiencyModel", secondary=lambda: class_has_proficiencies
    )

    features = relationship("FeatureModel", secondary=lambda: class_has_features)

    skills = relationship("SkillModel", secondary=lambda: class_has_skills)

    spells = relationship("SpellModel", secondary=lambda: class_has_spells)

    languages = relationship("LanguageModel", secondary=lambda: class_has_languages)

    # Relationship to PlayerChar

    def __repr__(self):
        return "<Class (name='%s', description='%s')>" % (
            self.class_name,
            self.class_descrip,
        )

    @classmethod
    def find_by_name(cls, class_name) -> "CharClassModel":
        return cls.query.filter_by(class_name=class_name).first()

    @classmethod
    def find_all(cls) -> List["CharClassModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
