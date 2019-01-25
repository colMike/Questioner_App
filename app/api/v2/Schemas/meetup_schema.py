from marshmallow import Schema, fields
from ...v2.utils.validators import Not_null_string

class MeetupSchema(Schema):
    """ Class to validate schema for Meetup object """
    
    location = fields.Str(required=True, validate= Not_null_string)
    meetup_images = fields.List(fields.Str(), required=False)
    topic = fields.Str(required=True, validate= Not_null_string)
    description = fields.Str(required=True, validate= Not_null_string)
    happeningOn = fields.Str(required=True, validate= Not_null_string)
    meetup_tags = fields.List(fields.Str, required=False)
    
    
class RsvpSchema(Schema):
    """ Class to validate schema for Meetup object """

    reply = fields.Str(required=True, validate= Not_null_string)

