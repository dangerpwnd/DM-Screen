from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

Class AttributeModel(Base):

    __tablename__ = 'attribute'

    # Columns
    id_attribute = Column(Integer, primary_key=True)
    attribute_name = Column(String(75), nullable=False)
    attribute_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__ = '<Attribute (name=%s, descrip=%s)>' %
        (self.attribute_name, self.attribute_descrip)

    @classmethod
    find_by_name(cls, attribute_name: str) -> AttributeModel:
        return cls.query.filter_by(attribute_name=attribute_name).first()

    @classmethod
    find_all(cls) -> List['AttributeModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()