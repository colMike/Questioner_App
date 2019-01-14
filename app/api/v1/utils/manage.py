"""Resource for shared functions"""

def fetch_one_meetup(meetups, meetupId):
    """Fetch specific item"""
    for meetup in meetups:
            if int(meetupId) == meetup['meetupId']:
                return meetup

def fetch_one_question(questions, questionId):
    """Fetch specific item"""
    for question in questions:
            if int(questionId) == question['questionId']:
                return question

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


            