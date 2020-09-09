from marshmallow import Schema, fields, post_load
from models.coin import CoinModel


class CoinSchema(Schema):
    id_coin = fields.Integer(dump_only=True)
    coin_name = fields.Str()
    coin_descrip = fields.Str()

    @post_load
    def make_coin(self, data, **kwargs):
        return CoinModel(**data)
