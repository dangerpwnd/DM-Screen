from flask_restful import Resource, request
from models.feature import FeatureModel
from schemas.feature import FeatureSchema

feature_schema = FeatureSchema()
feature_list_schema = FeatureSchema(many=True)

class Feature(Resource):

    @classmethod
    def get(cls, feature_name: str):
        feature = FeatureModel.find_by_name(feature_name)
        if not feature:
            return {'message': 'Feature not found.'}, 404
        return feature_schema.dump(feature), 200

    @classmethod
    def post(cls, feature_name: str):
        if FeatureModel.find_by_name(feature_name):
            return {'message': 'Feature with name "{}" already exists.'.format(feature_name)}

        feature_json = request.get_json()
        feature_json['feature_name'] = feature_name

        feature = feature_schema.load(feature_json)
        feature.save_to_db()
        return feature_schema.dump(feature), 201

    @classmethod
    def delete(cls, feature_name: str):
        feature = FeatureModel.find_by_name(feature_name)
        if feature:
            feature.delete_from_db()
            return {'message': 'Feature deleted.'}, 200

        return {'message': 'Feature not found.'}, 404

    @classmethod
    def put(cls, feature_name: str):
        feature_json = request.get_json()
        feature = FeatureModel.find_by_name(feature_name)

        if feature:
            feature.feature_descrip = feature_json['feature_descrip']
        else:
            feature_json['feature_name'] = feature_name
            feature = feature_schema.load(feature_json)

        feature.save_to_db()

        return feature_schema.dump(feature), 200

class FeatureList(Resource):

    @classmethod
    def get(cls):
        return {'Features': feature_list_schema.dump(FeatureModel.find_all())}
