from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.equipment import EquipmentModel

class Proficiency(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('descrip',
                        type=str,
                        required=True,
                        help="Proficiency requires descriptions!"
                        )

    @jwt_required
    def get(self, name):
        proficiency = ProficiencyModel.find_by_name(name)

        if proficiency:
            return proficiency.json()
        return {"message": "Proficiency not found."}, 404

    @jwt_required
    def post(self,name):
        if ProficiencyModel.find_by_name(name):
            return {"message": "Proficiency with name '{}' already exists.".format(name)}

        data = Proficiency.parser.parse_args()

        proficiency = ProficiencyModel(name, **data)

        try:
            proficiency.save_to_db()
        except:
            return {"message": "An error occurred inserting the proficiency."}, 500

        return proficiency.json(), 201

    @jwt_required
    def delete(self, name):
        proficiency = ProficiencyModel.find_by_name(name)

        if proficiency:
            proficiency.delete_from_db()
            return {"message": "Proficiency deleted"}

        return {"message": "Proficiency not found"}

    @jwt_required
    def put(self, name):
        data = Equipment.parser.parse_args()

        proficiency = ProficiencyModel.find_by_name(name)

        if proficiency is None:
            proficiency = ProficiencyModel(name, **data)
        else:
            proficiency.descrip = data['descrip']

        proficiency.save_to_db()

        return proficiency.json()

class ProficiencyList(Resource):
    @jwt_required
    def get(self):
        return {'Proficiency': [proficiency.json() for proficiency in ProficiencyModel.query.all()]}
