from flask_restful import Resource, request
from models.size import SizeModel
from schemas.size import SizeSchema

size_schema = SizeSchema()
size_list_schema = SizeSchema(many=True)

class Size(Resource):

    @classmethod
    def get(cls, size_name: str):
        size = SizeModel.find_by_name(size_name)
        if not size:
            return {"message": "Size not found."}, 404
        return size_schema.dump(size), 200

    @classmethod
    def post(cls, size_name: str):
        if SizeModel.find_by_name(size_name):
            return {"message": "Size with name '{}' already exists.".format(size_name)}

        size = SizeModel()
        size.size_name = size_name

        size.save_to_db()

        return size_schema.dump(size), 201

    @classmethod
    def delete(cls, size_name: str):
        size = SizeModel.find_by_name(size_name)

        if size:
            size.delete_from_db()
            return {"message": "Size deleted."}

        return {"message": "Size not found."}

    # put method not required as only one attribute

class SizeList(Resource):

    def get(cls):
        return {'Sizes': size_list_schema.dump(SizeModel.find_all())}
