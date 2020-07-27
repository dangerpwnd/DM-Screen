from db import db

class ToolModel(db.Model):

    # Set table name with class Attribute
    __tablename__ = "Tool"

    # Columns
    id_tool = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100), nullable=False)
    tool_descrip = db.Column(db.String(250), nullable=False)
    tool_weight = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_name(cls, tool_name):
        return cls.query.filter_by(tool_name=tool_name).first() # SELECT * FROM Tool WHERE name=name LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all();

    def save_to_db(self): # Handles insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
