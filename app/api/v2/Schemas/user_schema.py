from marshmallow import Schema, fields
from ...v2.utils.validators import Not_null_string, check_password, check_email, check_spaces_and_symbols     

class UserSignupSchema(Schema):
    """ Class to validate schema for Meetup object """    
    
    firstname = fields.Str(required=True,validate= [Not_null_string, check_spaces_and_symbols])
    lastname = fields.Str(required=True, validate= [Not_null_string, check_spaces_and_symbols])
    othername = fields.Str(required=False, validate= [Not_null_string, check_spaces_and_symbols])
    email = fields.Str(required=True, validate= [Not_null_string, check_email])
    phoneNumber = fields.Str(validate= [Not_null_string, check_spaces_and_symbols])
    username = fields.Str(required=False, validate= [Not_null_string, check_spaces_and_symbols])
    password = fields.Str(required=True, validate= [Not_null_string, check_password, check_spaces_and_symbols])

class UserLoginSchema(Schema):
    """ Class to validate schema for Meetup object """
    
    password = fields.Str(required=True, validate= Not_null_string)
    username = fields.Str(required=True, validate= Not_null_string)
       
    
    