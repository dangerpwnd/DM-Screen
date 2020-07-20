from db import db

class ToolModel(db.Model):

    # Set table name with class Attribute
    __tablename__ = "Tool"

    # Columns
    id_tool = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100), nullable=False)
    tool_descrip = db.Column(db.String(250), nullable=False)
    tool_weight = db.Column(db.Integer, nullable=False)

    def __init__(self, tool_name, tool_descrip, tool_weight):
        self.tool_name = tool_name
        self.tool_descrip = tool_descrip
        self.tool_weight = tool_weight

    def json(self):
        return {"name": self.tool_name, "descrip": self.tool_descrip, "weight": self.weight}

    @classmethod
    def find_by_name(cls, tool_name):
        return cls.query.filter_by(tool_name=tool_name).first() # SELECT * FROM Tool WHERE name=name LIMIT 1

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
