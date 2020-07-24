import ma from ma
from models.background import BackgroundModel

class BackgroundSchema(ma.ModelSchema):
    class Meta:
        model = BackgroundModel
        load_only = ('') #Need to determine what FK to use as
        dump_only = ('id_background',)
        include_fk = True
