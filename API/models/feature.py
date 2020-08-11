from typing import List
from db import Base, session
from models.race import RaceModel as race
from models.subrace import SubraceModel as subrace
from models.charclass import CharClassModel as classm

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class FeatureModel(Base):

    __tablename__ = 'Feature'

    # Columns
    id_feature = Column(Integer, primary_key=True)
    feature_name = Column(String(75), nullable=False, unique=True)
    feature_descrip = Column(String(250), nullable=False)

    # Association tables
    spell_assoc = Table('Feature_has_Spells', Base.metadata,
        Column('spell_id', Integer, ForeignKey('Spell.id_spell'), primary_key=True),
        Column('feature_id', Integer, ForeignKey('Feature.id_feature'), primary_key=True)
    )

    # Relationships
    races = relationship('RaceModel',
                                secondary=race.feature_assoc,
                                back_populates='features')

    subraces = relationship('SubraceModel',
                                secondary=subrace.feature_assoc,
                                back_populates='features')

    classes = relationship('ClassModel',
                                  secondary=classm.feature_assoc,
                                  back_populates='equipment')

    spells = relationship('SpellModel',
                            secondary=spell_assoc,
                            back_populates='features'
    )



    def __repr__ = '<Feature (name=%s, descrip=%s)>' %
        (self.feature_name, self.feature_descrip)

    @classmethod
    find_by_name(cls, feature_name: str) -> FeatureModel:
        return cls.query.filter_by(feature_name=feature_name).first()

    @classmethod
    find_all(cls) -> List['FeatureModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
