from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String

class CharAttributeModel(Base):

    __tablename__ = "Attribute"

    # Columns
    id_attribute = Column(Integer, primary_key=True)
    attribute_name = Column(String(75), nullable=False, unique=True)
    attribute_descrip = Column(String(250), nullable=False)

    def __repr__(self):
        return '<Attribute (name="%s", descrip="%s")>' % (
            self.attribute_name,
            self.attribute_descrip,
        )

    @classmethod
    def find_by_name(cls, attribute_name: str) -> "CharAttributeModel":
        return cls.query.filter_by(attribute_name=attribute_name).first()

    @classmethod
    def find_all(cls) -> List["CharAttributeModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
