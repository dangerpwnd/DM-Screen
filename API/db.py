from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://dm:YourNewGod@localhost/dnd5eDB")
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # Import all models first before creation to register properly on the metadata
    import models.armor
    import models.armortype
    import models.alignment
    import models.background
    import models.character
    import models.charattribute
    import models.charclass
    import models.coin
    import models.equipment
    import models.eye
    import models.faction
    import models.feat
    import models.feature
    import models.hair
    import models.language
    import models.proficiency
    import models.race
    import models.size
    import models.skill
    import models.skin
    import models.spell
    import models.spelltype
    import models.subclass
    import models.subrace
    import models.tool
    import models.trait
    import models.user
    import models.weapon
    import models.weapontype
    Base.metadata.create_all(engine)

metadata = init_db()
