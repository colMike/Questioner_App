"""User models"""

users = []


class UserModels:
    """The user Models Class"""
    def __init__(self):
        """Initializing the User Model Class"""
        pass

def add_user(self, username, email, password, confirm_password):
    """Adding New Users"""
    user_data = {
            'user_id': len(users) + 1,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
    }

    user_details = users.append(user_data)
    return user_details