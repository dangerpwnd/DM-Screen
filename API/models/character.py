from db import Base, session
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Association Tables

character_has_armor = Table(
    "Character_has_Armor",
    Base.metadata,
    Column("armor_id", Integer, ForeignKey("Armor.id_armor"), primary_key=True,),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_attributes = Table(
    "Character_has_Attributes",
    Base.metadata,
    Column(
        "charattribute_id",
        Integer,
        ForeignKey("Attribute.id_attribute"),
        primary_key=True,
    ),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_classes = Table(
    "Character_has_Classes",
    Base.metadata,
    Column("class_id", Integer, ForeignKey("Class.id_class"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_coins = Table(
    "Character_has_Coins",
    Base.metadata,
    Column("coin_id", Integer, ForeignKey("Coin.id_coin"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_equipment = Table(
    "Character_has_Equipment",
    Base.metadata,
    Column("equip_id", Integer, ForeignKey("Equipment.id_equip"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_factions = Table(
    "Character_has_Factions",
    Base.metadata,
    Column("faction_id", Integer, ForeignKey("Faction.id_faction"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_feats = Table(
    "Character_has_Feats",
    Base.metadata,
    Column("feat_id", Integer, ForeignKey("Feat.id_feat"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_subclasses = Table(
    "Character_has_Subclasses",
    Base.metadata,
    Column(
        "subclass_id", Integer, ForeignKey("SubClass.id_subclass"), primary_key=True
    ),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_tools = Table(
    "Character_has_Tools",
    Base.metadata,
    Column("tool_id", Integer, ForeignKey("Tool.id_tool"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_users = Table(
    "Character_has_Users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("User.id"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)

character_has_weapons = Table(
    "Character_has_Weapons",
    Base.metadata,
    Column("weapon_id", Integer, ForeignKey("Weapon.id_weapon"), primary_key=True),
    Column("character_id", Integer, ForeignKey("Character.id_character"), primary_key=True),
)


class CharacterModel(Base):

    __tablename__ = "Character"

    id_character = Column(Integer, primary_key=True)
    character_name = Column(String(80))
    character_descrip = Column(String(80))

    # relationships

    # many to one alignment - DONE
    # many to many armor - DONE
    armor = relationship("ArmorModel", secondary=lambda: character_has_armor)
    # many to one background - DONE
    # many to many charattribute - DONE
    attributes = relationship(
        "CharAttributeModel", secondary=lambda: character_has_attributes
    )
    # many to many charclass - DONE
    classes = relationship("CharClassModel", secondary=lambda: character_has_classes)
    # many to many coin - DONE
    coins = relationship("CoinModel", secondary=lambda: character_has_coins)
    # many to many equipment - DONE
    equipment = relationship("EquipmentModel", secondary=lambda: character_has_equipment)
    # many to one eye color - DONE
    # many to many faction - DONE
    factions = relationship("FactionModel", secondary=lambda: character_has_factions)
    # many to many feat - DONE
    feats = relationship("FeatModel", secondary=lambda: character_has_feats)
    # many to one hair color - DONE
    # many to one race - DONE
    # many to one skin color - DONE
    # many to many subclass - DONE
    subclasses = relationship("SubClassModel", secondary=lambda: character_has_subclasses)
    # many to one subrace - DONE
    # many to many tool - DONE
    tools = relationship("ToolModel", secondary=lambda: character_has_tools)
    # many to many user - DONE
    users = relationship("UserModel", secondary=lambda: character_has_users)
    # many to many weapon - DONE
    weapons = relationship("WeaponModel", secondary=lambda: character_has_weapons)

    def __repr__(self):
        return "<Character (name='%s', description='%s')>" % (self.name, self.descrip)

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
