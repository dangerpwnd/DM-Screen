from flask_restful import Resource, request
from models.skill import SkillModel
from schemas.skill import SkillSchema

skill_schema = SkillSchema()
skill_list_schema = SkillSchema(many=True)

class Skill(Resource):

    @classmethod
    def get(cls, skill_name: str):
        skill = SkillModel.find_by_name(skill_name)
        if not skill:
            return {'message': 'Skill not found.'}, 404
        return skill_schema.dump(skill), 200

    @classmethod
    def post(cls, skill_name: str):
        if SkillModel.find_by_name(skill_name):
            return {'message': 'Skill with name "{}" already exists.'.format(skill_name)}

        skill_json = request.get_json()
        skill_json['skill_name'] = skill_name

        skill = skill_schema.load(skill_json)
        skill.save_to_db()
        return skill_schema.dump(skill), 201

    @classmethod
    def delete(cls, skill_name: str):
        skill = SkillModel.find_by_name(skill_name)
        if skill:
            skill.delete_from_db()
            return {'message': 'Skill deleted.'}, 200

        return {'message': 'Skill not found.'}, 404

    @classmethod
    def put(cls, skill_name: str):
        skill_json = request.get_json()
        skill = SkillModel.find_by_name(skill_name)

        if skill:
            skill.skill_descrip = skill_json['skill_descrip']
        else:
            skill_json['skill_name'] = skill_name
            skill = skill_schema.load(skill_json)

        skill.save_to_db()

        return skill_schema.dump(skill), 200

class SkillList(Resource):

    @classmethod
    def get(cls):
        return {'Skills': skill_list_schema.dump(SkillModel.find_all())}
