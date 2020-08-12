from flask_restful import Resource, request
from models.alignment import AlignmentModel
from schemas.alignment import AlignmentSchema

alignment_schema = AlignmentSchema()
alignment_list_schema = AlignmentSchema(many=True)

class Alignment(Resource):

    @classmethod
    def get(cls, alignment_name: str):
        alignment = AlignmentModel.find_by_name(alignment_name)
        if not alignment:
            return {"message": "Alignment not found."}, 404
        return alignment_schema.dump(alignment), 200

    @classmethod
    def post(cls, alignment_name: str):
        if AlignmentModel.find_by_name(alignment_name):
            return {"message": "Alignment with name '{}' already exists.".format(alignment_name)}

        alignment_json = request.get_json()
        alignment_json["alignment_name"] = alignment_name

        alignment = alignment_schema.load(alignment_json)

        alignment.save_to_db()

        return alignment_schema.dump(alignment), 201

    @classmethod
    def delete(cls, alignment_name: str):
        alignment = AlignmentModel.find_by_name(alignment_name)

        if alignment:
            alignment.delete_from_db()
            return {"message": "Alignment deleted."}

        return {"message": "Alignment not found."}

    @classmethod
    def put(cls, alignment_name: str):
        alignment_json = request.get_json()
        alignment = AlignmentModel.find_by_name(alignment_name)

        if alignment:
            alignment.alignment_descrip = alignment_json['alignment_descrip']
        else:
            alignment_json['alignment_name'] = alignment_name
            alignment = alignment_schema.load(alignment_json)

        alignment.save_to_db()

        return alignment_schema.dump(alignment), 200

class AlignmentList(Resource):

    def get(cls):
        return {'Alignments': alignment_list_schema.dump(alignmentModel.find_all())}
