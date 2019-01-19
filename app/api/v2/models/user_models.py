"""User models"""
from app.api.v1.utils.manage import find_username, find_password, user_exists
from  instance.db_con import cur, con

users_list = []


class UserModels:
    """The user Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        pass

    def add_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        """Adding New Users"""
        # user_data = {
        #     "UserId": len(users_list) + 1,
        #     "firstname": firstname,
        #     "lastname": lastname,
        #     "othername": othername,
        #     "email": email,
        #     "phoneNumber": phoneNumber,
        #     "username": username,
        #     "registered": True,
        #     "isAdmin": False,
        #     "password": password
        # }
        """Check if user exists"""
        cur.execute("SELECT * FROM users WHERE username= %s",(username,))
        
        
        data = cur.fetchall()

        if not data:
            cur.execute(
                "INSERT INTO users(firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (firstname,
                lastname,
                othername,
                email,
                phoneNumber,
                username,
                True,
                False,
                password))

            con.commit()
            return 
        
        else:
            print("user already exists")

        # return users_list

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
