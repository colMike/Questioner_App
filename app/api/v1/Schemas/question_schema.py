from marshmallow import Schema, fields, validates
from ..utils.validators import Not_null_string


class QuestionSchema(Schema):
    """ Class to validate schema for Question object """

    createdBy = fields.Int(required=True)
    meetup = fields.Int(required=True)
    title = fields.Str(required=True, validate= Not_null_string)
    body = fields.Str(required=True, validate= Not_null_string)
    