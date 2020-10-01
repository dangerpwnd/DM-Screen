from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String


class TraitModel(Base):

    __tablename__ = "Trait"

    # Columns
    id_trait = Column(Integer, primary_key=True)
    trait_name = Column(String(100), nullable=False, unique=True)
    trait_descrip = Column(String(250), nullable=False)

    def __repr__(self):
        return "<Trait (name='%s', description='%s')>" % (
            self.trait_name,
            self.trait_descrip,
        )

    @classmethod
    def find_by_name(cls, trait_name) -> "TraitModel":
        return cls.query.filter_by(
            trait_name=trait_name
        ).first()  # SELECT * FROM Equipment WHERE name=name LIMIT 1

    @classmethod
    def find_by_id(cls, id_trait):
        return cls.query.filter_by(id_trait=id_trait).first()

    @classmethod
    def find_all(cls) -> List["TraitModel"]:
        return cls.query.all()

    def save_to_db(self):  # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
