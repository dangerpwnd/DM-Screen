from marshmallow import Schema, fields, post_load
from models.language import LanguageModel

class LanguageSchema(Schema):
    id_language = fields.Integer(dump_only=True)
    language_name = fields.Str()
    language_descrip = fields.Str()

    @post_load
    def make_language(self, data, **kwargs):
        return LanguageModel(**data)
