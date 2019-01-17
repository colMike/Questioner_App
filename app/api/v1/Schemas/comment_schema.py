from marshmallow import Schema, fields
from ..utils.validators import Not_null_string


class CommentSchema(Schema):
    """ Class to validate schema for Question Comment """        
    
    comment = fields.Str(required=True, validate= Not_null_string)
    