from marshmallow import Schema, fields
from ..utils.validators import Not_null_string


class QuestionSchema(Schema):
    """ Class to validate schema for Question object """

    createdBy = fields.Int(strict=True,required=True)
    meetup = fields.Int(strict=True, required=True)
    title = fields.Str(strict=True, required=True, validate= Not_null_string)
    body = fields.Str(strict=True, required=True, validate= Not_null_string)
    votes = fields.Int(strict=True, required=True)
    
    