# """Resource for shared functions"""
# import psycopg2     
# from instance.db_con import con_return
 
# con = con_return()
# cur = con.cursor()

# def fetch_one_meetup(meetups, meetupId):
#     """Fetch specific item"""
#     # for meetup in meetups:
#     #         if int(meetupId) == meetup['meetupId']:
#     #             return meetup


# def fetch_one_question(questionId):
#     """Fetch specific question"""
    
#     # cur.execute(
#     #     "SELECT * FROM questions WHERE questionId= %s", (questionId,))

#     # query = "SELECT * FROM questions WHERE questionId= '{}';".format(questionId)
#     # cur.execute(query)
#     # data = cur.fetchone()

#     # if data:
#     #     return data
#     # else:
#     #     return None


# def fetch_one_comment(comments, questionId):
#     # """Fetch specific question's comments"""
#     # for comment in comments:
#     #         if int(questionId) == comment['questionId']:
#     #             return comment


# def find_username(username):
#     """Find the username in the database"""
#     # cur.execute(
#     #     "SELECT * FROM users WHERE username= %s", (username))

#     # username_data = cur.fetchone()

#     # if username_data:
#     #     return True
#     # else:
#     #     return False


# def find_password(username, password):
#     # """Look if the password matches the one in the database"""
#     # cur.execute(
#     #     "SELECT * FROM users WHERE username= %s", (username))

#     # data = cur.fetchone()

#     # if data == None:
#     #     pass
#     # else:
#     #     """Get password from database"""
#     #     pass_in_db = data[9]
#     #     if pass_in_db == password:
#     #         return data
#     #     else:
#     #         return None 

# # def change_to_Admin(users_list, username):
    
# #     """Update user to admin"""
# #     for user in users_list:
# #         if username == user['username']:
# #             user.isAdmin = True
# #             return user


# def user_exists(username, email):
#     """Check if user exists"""
#     # cur.execute(
#     #     "SELECT * FROM users WHERE username= %s OR email = %s", (username, email))

#     # data = cur.fetchall()

#     # if data:
#     #     return True

#     # else:
#     #     return False
