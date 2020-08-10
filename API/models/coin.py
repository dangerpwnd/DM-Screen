from typing import List
from db import Base, session

from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

Class CoinModel(Base):

    __tablename__ = 'coin'

    # Columns
    id_coin = Column(Integer, primary_key=True)
    coin_name = Column(String(75), nullable=False)
    coin_descrip = Column(String(250), nullable=False)

    # Relationships

    def __repr__ = '<Coin (name=%s, descrip=%s)>' %
        (self.coin_name, self.coin_descrip)

    @classmethod
    find_by_name(cls, coin_name: str) -> CoinModel:
        return cls.query.filter_by(coin_name=coin_name).first()

    @classmethod
    find_all(cls) -> List['CoinModel']:
        return cls.query.all()

    save_to_db(self):
        session.add(self)
        session.commit()

    delete_from_db(self):
        session.delete(self)
        session.commit()
