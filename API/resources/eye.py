from flask_restful import Resource, request
from models.eye import EyeModel
from schemas.eye import EyeSchema

eye_schema = EyeSchema()
eye_list_schema = EyeSchema(many=True)

class Eye(Resource):

    @classmethod
    def get(cls, eye_color: str):
        eye = EyeModel.find_by_color(eye_color)
        if not eye:
            return {"message": "Eye color not found."}, 404
        return eye_schema.dump(eye), 200

    @classmethod
    def post(cls, eye_color: str):
        if EyeModel.find_by_color(eye_color):
            return {"message": "Eye with color '{}' already exists.".format(eye_color)}

        eye = EyeModel()
        eye.eye_color = eye_color

        eye.save_to_db()

        return eye_schema.dump(eye), 201

    @classmethod
    def delete(cls, eye_color: str):
        eye = EyeModel.find_by_color(eye_color)

        if eye:
            eye.delete_from_db()
            return {"message": "Eye deleted."}

        return {"message": "Eye not found."}

    # put method not required as only one attribute

class EyeList(Resource):

    def get(cls):
        return {'Eyes': eye_list_schema.dump(EyeModel.find_all())}
