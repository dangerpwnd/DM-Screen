from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class CharClassModel(Base):

    # Set table name with class attribute
    __tablename__ = "Class"

    # Columns
    id_class = Column(Integer, primary_key=True)
    class_name = Column(String(75), nullable=False, unique=True)
    class_descrip = Column(String(250), nullable=False)

    # Association Tables
    equip_assoc = Table(
        "Class_has_Equipment",
        Base.metadata,
        Column("equip_id", Integer, ForeignKey("Equipment.id_equip"), primary_key=True),
        Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
    )

    prof_assoc = Table(
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

    feature_assoc = Table(
        "Class_has_Features",
        Base.metadata,
        Column(
            "feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True
        ),
        Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
    )

    skill_assoc = Table(
        "Class_has_Skills",
        Base.metadata,
        Column("skill_id", Integer, ForeignKey("Skill.id_skill"), primary_key=True),
        Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
    )

    spell_assoc = Table(
        "Class_has_Spells",
        Base.metadata,
        Column("spell_id", Integer, ForeignKey("Spell.id_spell"), primary_key=True),
        Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
    )

    lang_assoc = Table(
        "Class_has_Languages",
        Base.metadata,
        Column(
            "language_id", Integer, ForeignKey("Language.id_language"), primary_key=True
        ),
        Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
    )

    # Relationships
    subclasses = relationship("SubClassModel", back_populates="charclass")

    equipment = relationship(
        "EquipmentModel", secondary=equip_assoc, back_populates="classes"
    )

    proficiencies = relationship(
        "ProficiencyModel", secondary=prof_assoc, back_populates="classes"
    )

    features = relationship(
        "FeatureModel", secondary=feature_assoc, back_populates="classes"
    )

    skills = relationship("SkillModel", secondary=skill_assoc, back_populates="classes")

    spells = relationship("SpellModel", secondary=spell_assoc, back_populates="classes")

    languages = relationship(
        "LanguageModel", secondary=lang_assoc, back_populates="classes"
    )

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
