from marshmallow import ValidationError

def Not_null_string(value):
    """Validate that string field under validation does not contain null value"""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value
    elif value:
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