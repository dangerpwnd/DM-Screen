from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship


class CoinModel(Base):

    __tablename__ = "coin"

    # Columns
    id_coin = Column(Integer, primary_key=True)
    coin_name = Column(String(75), nullable=False, unique=True)
    coin_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__(self):
        return '<Coin (name="%s", descrip="%s")>' % (self.coin_name, self.coin_descrip)

    @classmethod
    def find_by_name(cls, coin_name: str) -> CoinModel:
        return cls.query.filter_by(coin_name=coin_name).first()

    @classmethod
    def find_all(cls) -> List["CoinModel"]:
        return cls.query.all()

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
