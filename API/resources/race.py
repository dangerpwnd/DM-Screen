from flask_restful import Resource, request
from models.race import RaceModel
from schemas.race import RaceSchema

race_schema = RaceSchema()
race_list_schema = RaceSchema(many=True)


class Race(Resource):
    @classmethod
    def get(cls, race_name: str):
        race = RaceModel.find_by_name(race_name)
        if not race:
            return {"message": "Race not found."}, 404
        return race_schema.dump(race), 200

    @classmethod
    def post(cls, race_name: str):
        if RaceModel.find_by_name(race_name):
            return (
                {"message": 'A race with name "{}" already exists.'.format(race_name)},
                400,
            )

        race_json = request.get_json()
        race_json["race_name"] = race_name

        race = race_schema.load(race_json)

        race.save_to_db()

        return race_schema.dump(race), 201

    @classmethod
    def delete(cls, race_name: str):
        race = RaceModel.find_by_name(race_name)

        if race:
            race.delete_from_db()
            return {"message": "Race deleted."}

        return {"message": "Race not found."}, 404

    @classmethod
    def put(cls, race_name: str):
        race_json = request.get_json()
        race = RaceModel.find_by_name(race_name)

        if race:
            race.race_descrip = race_json["race_descrip"]
            race.race_min_age = race_json["race_min_age"]
            race.race_max_age = race_json["race_max_age"]
            race.race_min_height = race_json["race_min_height"]
            race.race_max_height = race_json["race_max_height"]
            race.race_speed = race_json["race_speed"]
        else:
            race_json["race_name"] = race_name
            race = race_schema.load(race_json)

        race.save_to_db()

        return race_schema.dump(race), 200


class RaceList(Resource):
    @classmethod
    def get(cls):
        return {"races": race_list_schema.dump(RaceModel.find_all())}, 200
