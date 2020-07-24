from ma import ma
from models import UserModel

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ('password',)
        dump_only = ('id',)
