from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String


class FeatModel(Base):

    __tablename__ = "Feat"

    # Columns
    id_feat = Column(Integer, primary_key=True)
    feat_name = Column(String(75), nullable=False, unique=True)
    feat_descrip = Column(String(250), nullable=False)

    def __repr__(self):
        return '<Feat (name="%s", descrip="%s")>' % (self.feat_name, self.feat_descrip)

    @classmethod
    def find_by_name(cls, feat_name: str) -> "FeatModel":
        return cls.query.filter_by(feat_name=feat_name).first()

    @classmethod
    def find_all(cls) -> List["FeatModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
