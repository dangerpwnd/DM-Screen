from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

# Association tables
feature_has_spells = Table(
    "Feature_has_Spells",
    Base.metadata,
    Column("spell_id", Integer, ForeignKey("Spell.id_spell"), primary_key=True),
    Column("feature_id", Integer, ForeignKey("Feature.id_feature"), primary_key=True),
)


class FeatureModel(Base):

    __tablename__ = "Feature"

    # Columns
    id_feature = Column(Integer, primary_key=True)
    feature_name = Column(String(75), nullable=False, unique=True)
    feature_descrip = Column(String(250), nullable=False)

    # Relationships

    spells = relationship("SpellModel", secondary=lambda: feature_has_spells)

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
