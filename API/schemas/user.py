from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.user import UserModel

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = UserModel
        load_instance = True
    id = auto_field(dump_only=True)
    username = auto_field()
    password = auto_field(load_only=True)
