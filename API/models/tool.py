from typing import List
from db import Base, session
from models.background import BackgroundModel as background

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ToolModel(Base):

    # Set table name with class Attribute
    __tablename__ = "Tool"

    # Columns
    id_tool = Column(Integer, primary_key=True)
    tool_name = Column(String(100), nullable=False, unique=True)
    tool_descrip = Column(String(250), nullable=False)
    tool_weight = Column(Integer, nullable=False)

    backgrounds = relationship(
        "BackgroundModel", secondary=background.tool_assoc, back_populates="tools"
    )

    def __repr__(self):
        return "<Tool (name='%s', description='%s', weight='%s')>" % (
            self.tool_name,
            self.tool_descrip,
            self.tool_weight,
        )

    @classmethod
    def find_by_name(cls, tool_name) -> "ToolModel":
        return cls.query.filter_by(
            tool_name=tool_name
        ).first()  # SELECT * FROM Tool WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls) -> List["ToolModel"]:
        return cls.query.all()

    def save_to_db(self):  # Handles insert and update
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()
