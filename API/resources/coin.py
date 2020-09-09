from flask_restful import Resource, request
from models.coin import CoinModel
from schemas.coin import CoinSchema

coin_schema = CoinSchema()
coin_list_schema = CoinSchema(many=True)


class Coin(Resource):
    @classmethod
    def get(cls, coin_name: str):
        coin = CoinModel.find_by_name(coin_name)
        if not coin:
            return {"message": "Coin not found."}, 404
        return coin_schema.dump(coin), 200

    @classmethod
    def post(cls, coin_name: str):
        if CoinModel.find_by_name(coin_name):
            return {"message": 'Coin with name "{}" already exists.'.format(coin_name)}

        coin_json = request.get_json()
        coin_json["coin_name"] = coin_name

        coin = coin_schema.load(coin_json)
        coin.save_to_db()
        return coin_schema.dump(coin), 201

    @classmethod
    def delete(cls, coin_name: str):
        coin = CoinModel.find_by_name(coin_name)
        if coin:
            coin.delete_from_db()
            return {"message": "Coin deleted."}, 200

        return {"message": "Coin not found."}, 404

    @classmethod
    def put(cls, coin_name: str):
        coin_json = request.get_json()
        coin = CoinModel.find_by_name(coin_name)

        if coin:
            coin.coin_descrip = coin_json["coin_descrip"]
        else:
            coin_json["coin_name"] = coin_name
            coin = coin_schema.load(coin_json)

        coin.save_to_db()

        return coin_schema.dump(coin), 200


class CoinList(Resource):
    @classmethod
    def get(cls):
        return {"Coins": coin_list_schema.dump(CoinModel.find_all())}
