from marshmallow import Schema, fields
from ..utils.validators import Not_null_string


class MeetupSchema(Schema):
    """ Class to validate schema for Meetup object """
    
    location = fields.Str(required=True, validate= Not_null_string)
    images = fields.List(fields.Str(), required=False)
    topic = fields.Str(required=True, validate= Not_null_string)
    happeningOn = fields.Str(required=True, validate= Not_null_string)
    tags = fields.List(fields.Str, required=False)
    
    
class RsvpSchema(Schema):
    """ Class to validate schema for Meetup object """
    
    id = fields.Int(required=True, validate= Not_null_string)
    meetup = fields.Int(required=True, validate= Not_null_string)
    user = fields.Int(required=True, validate= Not_null_string)
    response = fields.Str(required=True, validate= Not_null_string)

