from marshmallow import Schema, fields
from ..utils.validators import Not_null_string


class UserSignupSchema(Schema):
    """ Class to validate schema for Meetup object """    
    
    firstname = fields.Str(required=True, validate= Not_null_string)
    lastname = fields.Str(required=True, validate= Not_null_string)
    othername = fields.Str(required=False, validate= Not_null_string)
    email = fields.Str(required=True, validate= Not_null_string)
    phoneNumber = fields.Str(validate = Not_null_string)
    username = fields.Str(required=False)
    password = fields.Str(required=True, validate= Not_null_string)

class UserLoginSchema(Schema):
    """ Class to validate schema for Meetup object """
    
    password = fields.Str(required=True, validate= Not_null_string)
    username = fields.Str(required=True, validate= Not_null_string)
    
    
    