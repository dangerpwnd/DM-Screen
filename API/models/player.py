from db import Base, session
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Association Tables

player_has_armor = Table(
    "Player_has_Armor",
    Base.metadata,
    Column("armor_id", Integer, ForeignKey("Armor.id_armor"), primary_key=True,),
    Column("player_id", Integer, ForeignKey("PlayerChar.id_player"), primary_key=True),
)

player_has_attributes = Table(
    "Player_has_Attributes",
    Base.metadata,
    Column(
        "charattribute_id",
        Integer,
        ForeignKey("Attribute.id_attribute"),
        primary_key=True,
    ),
    Column("player_id", Integer, ForeignKey("PlayerChar.id_player"), primary_key=True),
)


class PlayerModel(Base):

    __tablename__ = "PlayerChar"

    id_player = Column(Integer, primary_key=True)
    player_name = Column(String(80))
    player_descrip = Column(String(80))

    # relationships

    # many to one alignment - DONE
    # many to many armor - DONE
    armor = relationship("ArmorModel", secondary=lambda: player_has_armor)
    # many to one background - DONE
    # many to many charattribute - DONE
    attributes = relationship(
        "CharAttributeModel", secondary=lambda: player_has_attributes
    )
    # many to many charclass
    # many to many coin
    # many to many equipment
    # many to one eye color
    # many to many faction
    # many to many feat
    # many to one hair color
    # many to one race
    # many to one skin color
    # many to many subclass
    # many to one subrace
    # many to many tool
    # many to one user
    # many to many weapon

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
