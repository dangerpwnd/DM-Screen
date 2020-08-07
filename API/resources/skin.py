from flask_restful import Resource, request
from models.skin import SkinModel
from schemas.skin import SkinSchema

skin_schema = SkinSchema()
skin_list_schema = SkinSchema(many=True)

class Skin(Resource):

    @classmethod
    def get(cls, skin_color: str):
        skin = SkinModel.find_by_color(skin_color)
        if not skin:
            return {"message": "Skin color not found."}, 404
        return skin_schema.dump(skin), 200

    @classmethod
    def post(cls, skin_color: str):
        if SkinModel.find_by_color(skin_color):
            return {"message": "Skin with color '{}' already exists.".format(skin_color)}

        skin_json = request.get_json()
        skin_json["skin_color"] = skin_color

        skin = skin_schema.load(skin_json)

        skin.save_to_db()

        return skin_schema.dump(skin), 201

    @classmethod
    def delete(cls, skin_color: str):
        skin = SkinModel.find_by_color(skin_color)

        if skin:
            skin.delete_from_db()
            return {"message": "Skin deleted."}

        return {"message": "Skin not found."}

    # put method not required as only one attribute

class SkinList(Resource):

    def get(cls):
        return {'Skins': skin_list_schema.dump(SkinModel.find_all())}
