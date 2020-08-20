from typing import List
from db import Base, session
from sqlalchemy import Column, Integer, String, Array, Table, ForeignKey
from sqlalchemy.orm import relationship


class BackgroundModel(Base):

    # Set table name with class attribute
    __tablename__ = "Background"

    # Columns
    id_background = Column(Integer, primary_key=True)
    background_name = Column(String(50), nullable=False, unique=True)
    background_descrip = Column(String(250), nullable=False)
    equip_id = Column(Array(Integer))
    proficiency_id = Column(Array(Integer))

    # Association Tables
    equip_assoc = Table(
        "Background_has_Equipment",
        Base.metadata,
        Column("equip_id", Integer, ForeignKey("Equipment.id_equip"), primary_key=True),
        Column(
            "background_id",
            Integer,
            ForeignKey("Background.id_background"),
            primary_key=True,
        ),
    )

    prof_assoc = Table(
        "Background_has_Proficiencies",
        Base.metadata,
        Column(
            "proficiency_id",
            Integer,
            ForeignKey("Proficiency.id_proficiency"),
            primary_key=True,
        ),
        Column(
            "background_id",
            Integer,
            ForeignKey("Background.id_background"),
            primary_key=True,
        ),
    )

    # Relationships linked to association tables
    equipment = relationship(
        "EquipmentModel", secondary=equip_assoc, back_populates="backgrounds"
    )

    proficiencies = relationship(
        "ProficiencyModel", secondary=prof_assoc, back_populates="backgrounds"
    )

    # Relationship to PlayerChar

    def __repr__(self):
        return "<Background (name='%s', description='%s')>" % (
            self.background_name,
            self.background_descrip,
        )

    @classmethod
    def find_by_name(cls, background_name) -> "BackgroundModel":
        return cls.query.filter_by(background_name=background_name).first()

    @classmethod
    def find_all(cls) -> List["BackgroundModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
