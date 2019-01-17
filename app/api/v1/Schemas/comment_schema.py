from marshmallow import Schema, fields
from ..utils.validators import Not_null_string


class CommentsSchema(Schema):
    """ Class to validate schema for Question Comment """    
    
    questionId = fields.Str(required=True, validate= Not_null_string)
    title = fields.Str(required=True, validate= Not_null_string)
    body = fields.Str(required=False, validate= Not_null_string)
    comment = fields.Str(required=True, validate= Not_null_string)
    phoneNumber = fields.Str(validate = Not_null_string)
    username = fields.Str(required=False)
    password = fields.Str(required=True, validate= Not_null_string)

    # "questionId": 1,
    # "title":   "Andela Bootcamp",
    # "body":   "This is an Andela bootcamp meeting",
    # "comment": "This is a very well thought out question"

    