"""Resource for shared functions"""
from instance.db_con import con, cur
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

def fetch_one_comment(comments, questionId):
    """Fetch specific question's comments"""
    for comment in comments:
            if int(questionId) == comment['questionId']:
                return comment

def find_username(users, username):
    """Find the username in the database"""
    for user in users:
        if username == user['username']:
            return user


def find_password(users_list, password):
    """Look if the password matches the one in the database"""
    for user in users_list:
        if password == user['password']:
            return user

def change_to_Admin(users_list, username):
    """Change a user to an Administrator"""
    for user in users_list:
        if username == user['username']:
            user.isAdmin = True
            return user

def user_exists(users_list, username, email):
    """Change a user to an Administrator"""


    for user in users_list:
        if username == user['username'] or email == user['email']:
            return True            
        else:
            return False
            