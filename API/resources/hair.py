from flask_restful import Resource, request
from models.hair import HairModel
from schemas.hair import HairSchema

hair_schema = HairSchema()
hair_list_schema = HairSchema(many=True)

class hair(Resource):

    @classmethod
    def get(cls, hair_color: str):
        hair = HairModel.find_by_color(hair_color)
        if not hair:
            return {"message": "Hair color not found."}, 404
        return hair_schema.dump(hair), 200

    @classmethod
    def post(cls, hair_color: str):
        if HairModel.find_by_color(hair_color):
            return {"message": "Hair with color '{}' already exists.".format(hair_color)}

        hair_json = request.get_json()
        hair_json["hair_color"] = hair_color

        hair = hair_schema.load(hair_json)

        hair.save_to_db()

        return hair_schema.dump(hair), 201

    @classmethod
    def delete(cls, hair_color: str):
        hair = HairModel.find_by_color(hair_color)

        if hair:
            hair.delete_from_db()
            return {"message": "Hair deleted."}

        return {"message": "Hair not found."}

    # put method not required as only one attribute

class HairList(Resource):

    def get(cls):
        return {'Hairs': hair_list_schema.dump(hairModel.find_all())}
