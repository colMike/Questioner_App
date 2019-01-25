import re
from marshmallow import ValidationError

def Not_null_string(value):
    """Validate that string field under validation does not contain null value"""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value
    elif value:
        return value

def check_email(email):
    """Check that email is in the right format"""
    if not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email):
        raise ValidationError('Invalid email format')

    return email

def check_spaces_and_symbols(value):
    """Check that field does not have unnecessary spaces or symbols"""
    if not re.match(r"(^[a-zA-z@#0-9]+$)", value):        
        raise ValidationError('Invalid parameter. Ensure there are no spaces in your field')
    return value



def check_password(password):
    """ Validate password is Strong """
    
    message = 'Your password is too weak'

    if len(password) < 6:
        raise ValidationError("Password must be 6 or more characters")

    rating = {}

    for character in password:
        if character.islower():
            rating['LowerCase'] = 1

        if character.isupper():
            rating['UpperCase'] = 1

        if character.isdigit():
            rating['Number'] = 1

    if sum(rating.values()) < 3:
        raise ValidationError(message)
        