from db import Base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ProficiencyModel(Base):

    __tablename__ = 'Proficiency'

    # Columns
    id_proficiency = Column(Integer, primary_key=True)
    proficiency_name = Column(String(100), nullable=False)
    proficiency_descrip = Column(String(250), nullable=False)

    backgrounds = relationship('BackgroundModel',
                                  secondary='Background_has_Proficiencies',
                                  back_populates='proficiencies')

    def __repr__(self):
        return "<Proficiency (name='%s', description='%s')>" % (
                                        self.proficiency_name,
                                        self.proficiency_descrip)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM Equipment WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
