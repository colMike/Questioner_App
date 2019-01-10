"""Resource for shared functions"""

def find_username(users, username):
    """Find the username in the database"""
    for user in users:
        if username == user['username']:
            return user


def find_password(users, password):
    """Look if the password matches the one in the database"""
    for user in users:
        if password == user['password']:
            return user