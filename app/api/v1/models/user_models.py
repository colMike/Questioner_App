"""User models"""

users = []


class UserModels:
    """The user Models Class"""
    def __init__(self):
        """Initializing the User Model Class"""
        pass

def add_user(self, firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin):
    """Adding New Users"""
    user_data = {
            "id": len(users) + 1,
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "registered": registered,
            "isAdmin": False
    }

    

    user_details = users.append(user_data)
    return user_details