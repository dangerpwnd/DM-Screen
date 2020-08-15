from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship


class AttributeModel(Base):

    __tablename__ = "attribute"

    # Columns
    id_attribute = Column(Integer, primary_key=True)
    attribute_name = Column(String(75), nullable=False, unique=True)
    attribute_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__(self):
        return '<Attribute (name="%s", descrip="%s")>' % (
            self.attribute_name,
            self.attribute_descrip,
        )

    @classmethod
    def find_by_name(cls, attribute_name: str) -> 'AttributeModel':
        return cls.query.filter_by(attribute_name=attribute_name).first()

    @classmethod
    def find_all(cls) -> List["AttributeModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
