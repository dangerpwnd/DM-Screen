from db import db

class ToolModel(db.Model):

    # Set table name with class Attribute
    __tablename__ = "Tool"

    # Columns
    id_tool = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100), nullable=False)
    tool_descrip = db.Column(db.String(250), nullable=False)
    tool_weight = db.Column(db.Integer, nullable=False)

    def __init__(self, name, descrip, weight):
        self.name = tool_name
        self.descrip = tool_descrip
        self.weight = tool_weight

    def json(self):
        return {"name": self.name, "descrip": self.descrip, "weight": self.weight}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM Tool WHERE name=name LIMIT 1

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
