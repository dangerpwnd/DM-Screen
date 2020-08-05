from db import Base, session
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    def __repr__(self):
        return "<User (username='%s')>" % (self.username)

    def save_to_db(self) -> None:
        session.add(self)
        session.commit()

    def delete_from_db(self) -> None:
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id) -> "UserModel":
        return cls.query.filter_by(id=_id).first()
