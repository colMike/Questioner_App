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


def find_username(username):
    """Find the username in the database"""
    cur.execute(
        "SELECT * FROM users WHERE username= %s", (username,))

    data = cur.fetchall()

    if data:
        return data
    else:
        return None
    
        

def find_password(username, password):
    """Look if the password matches the one in the database"""
    cur.execute(
        "SELECT * FROM users WHERE username= %s", (username,))

    data = cur.fetchone()
    print("******************")
    print(data)
    print("******************")

    """Get password from database"""
    pass_in_db = data[9]
    if pass_in_db == password:
        return True
    else:
        return False


def change_to_Admin(users_list, username):
    """Change a user to an Administrator"""
    for user in users_list:
        if username == user['username']:
            user.isAdmin = True
            return user


def user_exists(username, email):
    """Check if user exists"""
    cur.execute(
        "SELECT * FROM users WHERE username= %s OR email = %s", (username, email,))

    data = cur.fetchall()

    if data:
        return True

    else:
        return False
