from typing import List
from db import Base, session
from models.race import RaceModel as race

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class FeatureModel(Base):

    __tablename__ = 'Feature'

    # Columns
    id_feature = Column(Integer, primary_key=True)
    feature_name = Column(String(75), nullable=False)
    feature_descrip = Column(String(250), nullable=False)

    # Relationships
    races = relationship('RaceModel',
        secondary=race.feature_assoc,
        back_populates='features')

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
