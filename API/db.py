from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///player.db', convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # Import all models first before creation to register properly on the metadata
    import models.armor
    import models.armortype
    import models.alignment
    import models.attribute
    import models.background
    import models.coin
    import models.charclass
    import models.equipment
    import models.eye
    import models.faction
    import models.feat
    import models.feature
    import models.hair
    import models.language
    import models.player
    import models.proficiency
    import models.race
    import models.size
    import models.skill
    import models.skin
    import models.subclass
    import models.tool
    import models.user
    import models.weapon
    import models.weapontype

    Base.metadata.create_all(bind=engine)
