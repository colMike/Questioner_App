"""Resource for shared functions"""

def fetch_one(meetups, meetupId):
    """Fetch specific item"""
    for meetup in meetups:
            if int(meetupId) == meetup['meetupId']:
                return meetup

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