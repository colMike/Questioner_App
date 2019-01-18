"""User models"""
from app.api.v1.utils.manage import find_username, find_password, user_exists

"""Import the database """
from ..utils.database import db_conn, create_tables

users_list = []


class UserModels:
    """The user Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.db = db_conn()

    def add_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        """Adding New Users to the database"""
        user_data = {
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "registered": True,
            "isAdmin": False,
            "password": password
        }
        
        query_add = """"INSERT INTO users(FirstName, LastName, OtherName, Email, PhoneNumber, UserName, Registered, isAdmin, Password)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % \
        (user_data['firstname'], user_data['lastname'], user_data['othername'], user_data['email'], user_data['phonenumber'], user_data['username'], True, False, user_data['password'])
        
        save = self.db
        cur = save.cursor()
        cur.execute(query_add)
        save.commit()

        return user_data

    def find_by_username(self, username):
        """Find a user by username"""
        return find_username(users_list, username)

    def check_password(self, password):
        """Check if password matches"""
        return find_password(users_list, password)

    def check_exists(self, username, email):
        """"Check if a user already exists"""
        return user_exists(users_list, username, email)
    
    def get_all_users(self):
        """Return all meetups"""
        return users_list
