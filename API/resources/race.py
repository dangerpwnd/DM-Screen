from flask_restful import Resource, request
from models.race import RaceModel
from models.feature import FeatureModel
from models.language import LanguageModel
from models.proficiency import ProficiencyModel
from models.subrace import SubRaceModel
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
            race.size_id = race_json["size_id"]
        else:
            race_json["race_name"] = race_name
            race = race_schema.load(race_json)

        race.save_to_db()

        return race_schema.dump(race), 200


class RaceList(Resource):
    @classmethod
    def get(cls):
        return {"races": race_list_schema.dump(RaceModel.find_all())}, 200


class RaceHasLanguages(Resource):
    @classmethod
    def post(cls, race_name: str, language_name: str):
        race = RaceModel.find_by_name(race_name)
        language = LanguageModel.find_by_name(language_name)
        if not race:
            return {"message": "Race not found."}, 404
        if not language:
            return {"message": "Language not found."}, 404
        race.languages.append(language)
        race.save_to_db()
        return (
            {"message": "Language '{}' added.".format(language.language_name)},
            200,
        )


class RaceHasSubraces(Resource):
    @classmethod
    def post(cls, race_name: str, subrace_name: str):
        race = RaceModel.find_by_name(race_name)
        subrace = SubRaceModel.find_by_name(subrace_name)
        if not race:
            return {"message": "Race not found."}, 404
        if not subrace:
            return {"message": "Subrace not found."}, 404
        race.subraces.append(subrace)
        race.save_to_db()
        return (
            {"message": "Subrace '{}' added.".format(subrace.subrace_name)},
            200,
        )

class RaceHasTraits(Resource):
    @classmethod
    def post(cls, race_name: str, trait_name: str):
        race = RaceModel.find_by_name(race_name)
        trait = TraitModel.find_by_name(trait_name)
        if not race:
            return {"message": "Race not found."}, 404
        if not trait:
            return {"message": "Trait not found."}, 404
        race.proficiencies.append(trait)
        race.save_to_db()
        return (
            {"message": "Trait '{}' added.".format(trait.trait_name)},
            200,
        )