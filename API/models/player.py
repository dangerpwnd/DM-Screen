from db import Base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class PlayerModel(Base):

    __tablename__ = "PlayerChar"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    descrip = Column(String(80))

    def __repr__(self):
        return "<Player (name='%s', description='%s')>" % (self.name, self.descrip)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(
            name=name
        ).first()  # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):  # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
