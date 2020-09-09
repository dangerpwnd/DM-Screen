from marshmallow import Schema, fields, post_load
from models.user import UserModel


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str()
    password = fields.Str(load_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return UserModel(**data)
