from flask_restful import Resource, request
from models.faction import FactionModel
from schemas.faction import FactionSchema

faction_schema = FactionSchema()
faction_list_schema = FactionSchema(many=True)

class Faction(Resource):

    @classmethod
    def get(cls, faction_name: str):
        faction = FactionModel.find_by_name(faction_name)
        if not faction:
            return {'message': 'Faction not found.'}, 404
        return faction_schema.dump(faction), 200

    @classmethod
    def post(cls, faction_name: str):
        if FactionModel.find_by_name(faction_name):
            return {'message': 'Faction with name "{}" already exists.'.format(faction_name)}

        faction_json = request.get_json()
        faction_json['faction_name'] = faction_name

        faction = faction_schema.load(faction_json)
        faction.save_to_db()
        return faction_schema.dump(faction), 201

    @classmethod
    def delete(cls, faction_name: str):
        faction = FactionModel.find_by_name(faction_name)
        if faction:
            faction.delete_from_db()
            return {'message': 'Faction deleted.'}, 200

        return {'message': 'Faction not found.'}, 404

    @classmethod
    def put(cls, faction_name: str):
        faction_json = request.get_json()
        faction = FactionModel.find_by_name(faction_name)

        if faction:
            faction.faction_descrip = faction_json['faction_descrip']
        else:
            faction_json['faction_name'] = faction_name
            faction = faction_schema.load(faction_json)

        faction.save_to_db()

        return faction_schema.dump(faction), 200

class FactionList(Resource):

    @classmethod
    def get(cls):
        return {'Factions': faction_list_schema.dump(FactionModel.find_all())}
