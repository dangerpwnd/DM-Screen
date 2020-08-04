from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///player.db', convert_unicode=True)
db_session = scope_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import all models first before creation to register properly on the metadata
    import models.background
    import models.equipment
    import models.helper
    import models.player
    import models.proficiency
    import models.tool
    import models.user

    Base.metadata.create_all(bind=engine)
